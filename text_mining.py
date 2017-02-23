"""
Text_Mining by Seungin Lyu
Conducts sentiment anaylsis of all tweets of EPL players listed by
"Preimer Leauge Players"(public BBC Tweeter list) who have unprotected
timelines. The results for each indivual players are groupd by clubs to create
club sentiment anaylsis data for each of the EPL clubs.
"""

#  Data Sources
import twitter
import wikipedia
from bs4 import BeautifulSoup
import warnings


# Text Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import doctest
import datetime
import re
from pickle import dump, load
from os.path import exists
from os import mkdir


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
                pass  # when Exception occurs, just ignore the player.
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
    """
    Returns a dictionary with
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


def save_clubs_dictionary(filename, players):
    """
    Returns a dictionary that uses player names as keys, the clubs as values.
    (Tells you which club a player belongs to)
    Fetches the "current_team" using Wikipedia and beautifulsoup4.
    Beautifulsoup4 finds the first "td" element with class "org"
    which is the "current team" infomation found in wikipedia's infoboxes.
    CAUTION : This function isn't totally reliable
    (there might not exist any wikipedia page for cetain players).
    When an exception occurs, "unknown" become the value for the key.
    CAUTION2 : THIS MIGHT TAKE MORE THAN 10 MIUTES DUE TO SLOW RESPONSE RATE
    OF WIKIPEDIA SERVER
    """
    clubs_dictionary = dict()
    for player in players:
        player_name = player.name
        try:
            page = wikipedia.page(player_name)
            soup = BeautifulSoup(page.html(), "lxml")
            club = soup.find("td", class_="org").get_text().strip()
        except Exception:  # if the search fails, club is 'unknown'
            club = 'unknown'
        finally:
            clubs_dictionary[player_name] = club

    f = open(filename, 'wb')
    try:
        dump(clubs_dictionary, f)
    finally:
        f.close()


def load_clubs_dictionary(filename):
    """
    Returns the dictionary of clubs and players
    """
    f = open(filename, 'rb')
    clubs = dict()
    try:
        clubs = load(f)  # loads the number of players
    finally:
        f.close()
        return clubs


def club_nltk_analysis(players_nltk_results, club_dictionary):
    """
    Returns the sum of all NLTK_analysis results for EPL clubs as dictionary
    ex) {ManU : [0,0,0,0],
         ManCity : [0,0,0,0]}
    """
    club_analysis = dict()
    epl_clubs = ['AFC Bournemouth', 'Arsenal', 'Burnley', 'Chelsea',
                 'Crystal Palace', 'Everton', 'Hull City', 'Leicester City',
                 'Liverpool', 'Manchester City', 'Manchester United',
                 'Middlesbrough', 'Southampton', 'Stoke City', 'Sunderland',
                 'Swansea City', 'Tottenham Hotspur', 'Watford',
                 'West Bromwich Albion', 'West Ham United']
    for club in epl_clubs:
        club_analysis[club] = [0, 0, 0, 0]
    for player_name in players_nltk_results:
        for club in epl_clubs:
            # startswith method is used here for texts like..
            # ex) Current Team : 'Aresenal(on transfer from XX)'
            if club_dictionary[player_name].startswith(club):
                club_analysis[club][0] += players_nltk_results[player_name][0]
                club_analysis[club][1] += players_nltk_results[player_name][1]
                club_analysis[club][2] += players_nltk_results[player_name][2]
                club_analysis[club][3] += players_nltk_results[player_name][3]
    return club_analysis


def sorted_by_key(analysis_dictionary, list_index):
    """
    Returns a list of EPL clubs by the order of elements in
    specified "list_index" in "key dictionary" from club_nltk_analysis
    key: 0 (compound),1(neg),2(neu),3(pos)
    """
    return sorted(analysis_dictionary.keys(),
                  key=lambda k: analysis_dictionary[k][list_index],
                  reverse=True)


if __name__ == '__main__':
    doctest.testmod()

    # mutes deprecationWarning when using BeautifulSoup Package
    warnings.simplefilter("ignore", DeprecationWarning)
    # --------------------------------------------------------------------------
    # Part 0 -> Credentials for Twitter API Access
    credentials = get_credentials("keys.txt")  # Twitter API Credentials
    CONSUMER_KEY = credentials[0]
    CONSUMER_SECRET = credentials[1]
    ACCESS_TOKEN_KEY = credentials[2]
    ACCESS_TOKEN_SECRET = credentials[3]
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    # --------------------------------------------------------------------------
    # Part 1 -> Pickles Twitter 'user instances' of all epl_players
    #           listed in a Twitter List(EPL Players, Official BBC list)
    players_data = 'epl_players.pickle'
    if not exists(players_data):
        save_epl_members_list(players_data, api)
    # list of all player instances
    all_players = load_epl_members_list(players_data)

    # --------------------------------------------------------------------------
    # Part 2 -> Pickles Twitter 'status instances' for all 'user instances'
    for player in all_players:
        #  pickles status data for users with unprotected timelines
        status_data = "players_status/" + player.name
        if not exists(status_data) and not player.protected:
            save_tweets(player.id, player.name, api)

    # --------------------------------------------------------------------------
    # Part 3 -> Pickles tweet texts of status instances(unprotected timeline)
    # Texts are processed so that tags, hashtags, htmls are elimimnated.
    # Only Tweets from the first day of EPL16-17 season is saved.
    # The maximum number of status instances for each user insnaces is 200

    # First Day of EPL16-17
    START_TIME = datetime.datetime.strptime("Sat Aug 13 00:00:00 +0000 2016",
                                            '%a %b %d %X %z %Y')
    tweets_data = 'epl_players_tweets.pickle'
    if not exists(tweets_data):
        save_tweets_texts(tweets_data, all_players)
    tweet_texts = load_tweets_texts(tweets_data)  # Processed tweet texts

    # --------------------------------------------------------------------------
    # Part 4 -> Conducts Sentimental Analysis(NLTK)
    #           with tweet texts of all user instnaces with unprotected
    #           timelines. (Tweets of EPL Players with open timelines)
    nltk_results = all_players_nltk_analysis(all_players, tweet_texts)

    # --------------------------------------------------------------------------
    # Part 5 -> Regroups the NLTK results by EPL Clubs.
    #           Pickles current club of of a player from Wikipedia
    #           by using Wikipedia and BeautifulSoup package.
    #           (as a dictoinary that maps a player to a club)
    clubs_data = 'epl_clubs_players.pickle'
    if not exists(clubs_data):
        save_clubs_dictionary(clubs_data, all_players)
    clubs_dict = load_clubs_dictionary(clubs_data)
    club_analysis_results = club_nltk_analysis(nltk_results, clubs_dict)
    # --------------------------------------------------------------------------
    # Part 6 -> Displays results sorted by different sentiments of NLTK
    #           Keys : compound, neg, neu, pos
    print(sorted_by_key(club_analysis_results, 0))  # key = compound
    print(sorted_by_key(club_analysis_results, 1))  # key = neg
    print(sorted_by_key(club_analysis_results, 2))  # key = neu
    print(sorted_by_key(club_analysis_results, 3))  # key = pos
