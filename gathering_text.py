import twitter
import api_keys
import pickle
import re
from pathlib import Path


def print_tweet(tweet_num):
    my_file = Path('trumptwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('trumptwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        reloaded_copy_of_texts = [s + ' ' for s in reloaded_copy_of_texts]
        str_copy = str(reloaded_copy_of_texts)
        word1 = " ".join(re.findall("[a-zA-Z]+",
                                    str_copy))
        # print(word1)
        # reloaded_copy_of_texts.encode('utf-8').strip()
        print(word1)
        word1 = word1.split()
        my_dict = wordListToFreqDict(word1)
        sorted_dict = sortFreqDict(my_dict)
        for val in sorted_dict:
            print(val)
    else:
        retrieve_tweets()


def retrieve_tweets():

    api = twitter.Api(api_keys.consumer_key, api_keys.consumer_secret,
                      api_keys.access_token_key,
                      api_keys.access_token_secret)

    tweets = api.GetUserTimeline(screen_name='@realDonaldTrump', count=199,
                                 max_id='796130213826621440')
    for status in tweets:
        print(status.id)
        print(status.created_at)
    tweets = [s.text for s in tweets]
    # print(tweets)
    # Save data to a file (will be part of your data fetching script)
    f = open('trumptwitters.pickle', 'wb')
    pickle.dump(tweets, f)
    f.close()


# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    return aux
