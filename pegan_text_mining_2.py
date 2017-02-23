'''
    Alisha Pegan
    Software Design Spring 2017 Text Mining Assignment
    Code that produces the top 'n' twitter users that have tweeted a postive
    sentiment containing a specific hashtag
    The user inputs the hashtag, and n usernames
    The code outputs top n twitter usersnames that the person can follow
    '''
import os
import tweepy
from tweepy import Cursor
from tweepy import API
from tweepy import OAuthHandler
import time
import pandas
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# bring in the twitter app keys
from twitter_knock import Consumer_Key, Consumer_Secret, Access_Token, Access_Secret
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Secret)

# set how many tweets to get
tweet_count = 1000
# ensure that i do not go over rate limit
api = tweepy.API(auth, wait_on_rate_limit=True)


def pop_tweeters(hashtag_input, list_number):
    '''
    function called pop_tweeters to show top tweeters with the
    most followers who tweet about a certain topic
    '''
    # input a hashtag and number
    hashtag = str(hashtag_input)
    number = int(list_number)
    # use twitter api to gather all tweets that contain the hashtag
    data = Cursor(api.search, q=hashtag).items(tweet_count)

    tweets = []
    # forms a list with sub dictionaries with usernames, timestamp, text, and
    # number of followers
    for tweet in data:
        temp_dic = {}
        temp_dic['username'] = tweet.user.screen_name
        temp_dic['timestamp'] = tweet.created_at
        temp_dic['text'] = tweet.text
        temp_dic['followers'] = tweet.user.followers_count
        tweets.append(temp_dic)

    # pickle the tweet data
    f = open('hashtags.pickle', 'wb')
    pickle.dump(tweets, f)
    f.close()

    # open up the pickle
    # odd to do it here, i know
    input_file = open('hashtags.pickle', 'rb')
    tweet_data = pickle.load(input_file)
    input_file.close()

    # load the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # for every tweet, add another dictionary for sentiment
    for tweet in tweet_data:
        tweet['sentiment'] = analyzer.polarity_scores(tweet['text'])
    # positive is a list to store all the positive tweets
    positive = [tweet for tweet in tweet_data if tweet['sentiment']['pos'] > 0]
    # note: tranformation in the beginning, filtering at the end
    # sort the list by followers, highest to lowest
    top = sorted(positive, key=lambda tweet: tweet['followers'], reverse=True)
    # print the total sample pool
    print('The total sample size is', len(tweet_data))
    # print the top n usernames and the number of followers
    print('The top', number, 'popular Twitter usernames posting about', hashtag, 'are:')
    for tweet in top[: number]:
        print(tweet['username'], ',', tweet['followers'])


pop_tweeters('#urbandesign', 10)
