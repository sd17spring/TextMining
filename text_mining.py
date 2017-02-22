"""
Text_Mining by Seungin Lyu
Conducts sentiment anaylsis of all tweets of EPL players
and returns the combined results for each club in EPL 2016-2017.
"""

import doctest
import twitter
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
    Pickles the twitter user instance for each player
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


def club_of_this_player(player_name):
    """
    Returns the current club that the player with "player_name" belongs to.
    This uses a predefined dictionary that uses the player name as the key.
    The data for the dictionary comes from the offical EPL website
    https://www.premierleague.com/news/84136, posted on 01.09.2016"
    Returns the name with the closest string matching rate.
    """


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


def individual_player_nltk_analysis(player_name):
    """
    Returns the sum of all NLTK_analysis results of player_name as dictionary
    ex) {compound : 0.8439, neg : 0.0, neu : 0.248, pos : 0.752}
    """
    pass


def all_players_nltk_analysis(player_name):
    """
    Returns a dictionary with.
    key : player name
    value : individual player_nltk analysis
    ex) {Paul Pogba : {compound : 0.8439, neg : 0.0, neu : 0.248, pos : 0.752},
         Harry Kane : {compound : 0.8439, neg : 0.0, neu : 0.248, pos : 0.752}}
    """
    pass


def club_nltk_analysis():
    """
    Returns the sum of all NLTK_analysis results by clubs as dictionary
    ex) {ManU : {compound : 0.8439, neg : 0.0, neu : 0.248, pos : 0.752},
         ManCity : {compound : 0.8439, neg : 0.0, neu : 0.248, pos : 0.752}}
    """
    pass


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
    players = load_epl_members_list(players_data)  # list of player names
    for player in players:
        #  pickles status data for unprotected users
        status_data = "players_status/" + player.name
        if not exists(status_data) and not player.protected:
            save_tweets(player.id, player.name, api)
