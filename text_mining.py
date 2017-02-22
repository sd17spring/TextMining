"""
Text_Mining by Seungin Lyu
Conducts sentiment anaylsis of all tweets of EPL players
and returns the combined results for each club in EPL 2016-2017.
"""

import doctest
import twitter


def get_credentials(filename):
    """
    Returns credentials for twitter api from file with filename
    """
    pass


def save_epl_members_list(filename):
    """
    Pickles tuples of (name,twitter_id) of
    all members of "Premier League Players" Twitter list(public list by BBC)
    into a binary file "filename" that can be loaded with load_epl_members_list
    """
    pass


def load_epl_members_list(filename):
    """
    Returns a list of previous pickled tuples of EPL players.
    """
    pass


def follow_all_members_in_list(list_of_members, credentials):
    """
    Make the twitter account to follow all the members of a list automatically
    (so that manually following each member is unnecessary, and Twitter API
    requires that you follow the person to retrieve the tweets"
    """


def club_of_this_player(player_name):
    """
    Returns the current club that the player with "player_name" belongs to.
    This uses a predefined dictionary that uses the player name as the key.
    The data for the dictionary comes from the offical EPL website
    https://www.premierleague.com/news/84136, posted on 01.09.2016"
    Returns the name with the closest string matching rate.
    """


def save_tweets(player_name, start_time, end_time):
    """
    Creates file "player_tweets\player_name.txt" that contains all the Tweets
    of player_name from start_time to end_time.
    """


def load_tweets(player_name):
    """
    Returns a list of all pickled tweets of player with player_name
    """


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
    api = twitter.Api(credentials)
    print(api.GetUserTimeline(screen_name='anto_v25'))
