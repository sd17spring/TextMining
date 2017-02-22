"""
Text_Mining by Seungin Lyu
Conducts sentiment anaylsis of all tweets of EPL players listed by
"Preimer Leauge Players"(public BBC Tweeter list) who have unprotected
timelines. The results for each indivual players are groupd by clubs to create
club sentiment anaylsis data for each of the EPL clubs.
"""

import doctest
import twitter
import wikipedia
import datetime
import re
from pickle import dump, load
from os.path import exists
from os import mkdir
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup


def get_credentials(filename):
    """
    Returns credentials for twitter api from file with filename
    """
    f = open('keys.txt')
    keys = f.readlines()
    # codes from Oliver Steele's Piazza Class notes : keeping secrets
    credentials = []
    try:
        for line in keys:
            credentials.append(line.strip())
    finally:
        f.close()
    return credentials


def save_epl_members_list(filename, api):
    """
    Retrieves sequence of twitter.user.User instances of
    "Premier League Players" Twitter list(public list by BBC) as a list
    (This list might not be completely up to date, so not every member
    of this list still players in the EPL)
    Then Pickles the twitter user instance for each player.
    """
    epl_players = api.GetListMembers(None, 'premier-league-players',
                                     None, 'BBCSport')
    f = open(filename, 'wb')
    dump(len(epl_players), f)  # saves the number of players
    try:
        for each_player in epl_players:
            dump(each_player, f)
    finally:
        f.close()


def load_epl_members_list(filename):
    """
    Returns a list of previous pickled user instances of EPL players
    """
    f = open(filename, 'rb')
    players = []
    num_players = load(f)  # loads the number of players
    try:
        for i in range(num_players):
            players.append(load(f))
    finally:
        f.close()
        return players


def save_tweets(player_id, player_name, api):
    """
    Pickles file "players_status"/player_name.pickle" of
    200 latest Status Instances of player with player_id.
    200 is the maximum number of tweets limited by Twitter Api.
    """
    #  pickles the latest 200(max limit) statuses for each player
    statuses = api.GetUserTimeline(user_id=player_id, count=200)
    if not exists("players_status"):
        mkdir("players_status")
    f = open("players_status/" + player_name, 'wb')
    dump(len(statuses), f)  # saves the number of total Tweets
    try:
        for status in statuses:
            dump(status, f)
    finally:
        f.close()


def load_tweets(player_name):
    """
    Returns a list of all pickled Status Instances of player with player_name
    """
    f = open("players_status/" + player_name, 'rb')
    statuses = []
    num_status = load(f)  # loads the number of players
    try:
        for i in range(num_status):
            statuses.append(load(f))
    finally:
        f.close()
        return statuses


def get_texts_from_player(player_name, start_date):
    """
    Returns only texts that were created after time object "start_date"
    from a player(identified with player_name)'s statuses
    from the pickled files.
    Eliminates Tags('@'), Hashtags(#)
    and URLs that are irrelevant to text sentiment.
    """
    statuses = load_tweets(player_name)
    player_texts = []
    for status in statuses:
        status_time = datetime.datetime.strptime(status.created_at,
                                                 '%a %b %d %X %z %Y')
        if status_time >= start_date:
            #  regular expression that eliminates URL and @,
            #  source :
            #  http://stackoverflow.com/questions/8376691/
            #  how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression
            text = status.text
            text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                          "", text)
            player_texts.append(text)
    return player_texts


def save_tweets_texts(filename, players):
    """
    Pickles the collection of refined texts for players as a dictionary.
    in file (filename)
    """
    tweet_texts = dict()  # dictionary of all refined texts.
    # initializing the dictionary
    for player in players:
        if not player.protected:
            try:
                tweet_texts[player.name] = get_texts_from_player(player.name,
                                                                 START_TIME)
            except Exception:
                pass
    f = open(filename, 'wb')
    try:
        dump(tweet_texts, f)
    finally:
        f.close()


def load_tweets_texts(filename):
    """
    Returns the dictionary of all tweets texts
    """
    f = open(filename, 'rb')
    texts = dict()
    try:
        texts = load(f)  # loads the number of players
    finally:
        f.close()
        return texts


def player_nltk_analysis(player_name, texts):
    """
    Returns the sum of all NLTK_analysis results of player_name as
    lists of sentiment anaylsis [compound, neg, neu, pos]
    ex) [0.8439, 0.0, 0.248, 0.752]
    """
    analyzer = SentimentIntensityAnalyzer()
    nltk_analysis = [0, 0, 0, 0]
    for text in texts:
        scores = analyzer.polarity_scores(text)
        nltk_analysis[0] += scores['compound']
        nltk_analysis[1] += scores['neg']
        nltk_analysis[2] += scores['neu']
        nltk_analysis[3] += scores['pos']
    return nltk_analysis


def all_players_nltk_analysis(player_list, tweet_texts):
    """s
    Returns a dictionary with.
    key : player name
    value : individual player_nltk analysis [compound, neg, neu, pos]
    ex) {'Paul Pogba' : [0.8439, : 0.0, 0.248, 0.752]}
         'Harry Kane' : [0.8439, : 0.0, 0.248, 0.752]}
    """
    result = dict()
    for player in player_list:
        if not player.protected:
            name = player.name
            result[name] = player_nltk_analysis(name,
                                                tweet_texts[player.name])
    return result


def club_of_this_player(player_name):
    """
    Returns the current club that the player with "player_name" belongs to.
    Fetches the "current_team" using Wikipedia and beautifulsoup4
    Beautifulsoup4 is used to find the first "td" element with class "org"
    which stands for the current team in wikipedia's infoboxes.
    CAUTION : This function isn't totally reliable
    (there might not exist any wikipedia page for cetain players)

    """
    page = wikipedia.page(player_name)
    soup = BeautifulSoup(page.html(), "lxml")
    team = soup.find("td", class_="org").get_text().strip()
    return team


def club_nltk_analysis(players_nltk_results):
    """
    Returns the sum of all NLTK_analysis results by clubs as dictionary
    ex) {ManU : [0,0,0,0],
         ManCity : [0,0,0,0]}
    """
    epl_clubs = ['AFC Bournemouth', 'Arsenal', 'Burnley', 'Chelsea',
                 'Crystal Palace', 'Everton', 'Hull City', 'Leicester City',
                 'Liverpool', 'Manchester City', 'Manchester United',
                 'Middlesbrough', 'Southampton', 'Stoke City', 'Sunderland',
                 'Swansea City', 'Tottenham Hotspur', 'Watford',
                 'West Bromwich Albion', 'West Ham United']
    club_analysis = dict()
    for player_name in players_nltk_results:
        try:
            club = club_of_this_player(player_name)
            if club in epl_clubs:
                club_analysis[club] += nltk_results[player_name]
        except Exception:
            pass

    return club_analysis


def sort_by_key(key):
    """
    Returns a list of EPL clubs by the order of "key" from club_nltk_analysis
    keys : "compound, neg, neu, pos"
    text_analysis dictionary
    """
    pass


if __name__ == '__main__':
    doctest.testmod()
    credentials = get_credentials("keys.txt")
    CONSUMER_KEY = credentials[0]
    CONSUMER_SECRET = credentials[1]
    ACCESS_TOKEN_KEY = credentials[2]
    ACCESS_TOKEN_SECRET = credentials[3]
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    players_data = 'epl_players.pickle'
    if not exists(players_data):  # pickles only once if data doesn't exist
        save_epl_members_list(players_data, api)
    # list of all player instances
    all_players = load_epl_members_list(players_data)
    for player in all_players:
        #  pickles status data for users with unprotected timelines
        status_data = "players_status/" + player.name
        if not exists(status_data) and not player.protected:
            save_tweets(player.id, player.name, api)
    # First Day of EPL16-17
    START_TIME = datetime.datetime.strptime("Sat Aug 13 00:00:00 +0000 2016",
                                            '%a %b %d %X %z %Y')
    tweets_data = 'epl_players_tweets.pickle'
    if not exists(tweets_data):
        save_tweets_texts(tweets_data, all_players)
    tweet_texts = load_tweets_texts(tweets_data)  # Processed tweet texts
    nltk_results = all_players_nltk_analysis(all_players, tweet_texts)
    club_analysis_results = club_nltk_analysis(nltk_results)  # need to pickle
