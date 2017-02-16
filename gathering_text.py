import twitter
import api_keys
import pickle
import re
from pathlib import Path


def get_trump_tweets():
    my_file = Path('trumptwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('trumptwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@realDonaldTrump', 'trumptwitters.pickle',
                        '796130213826621440')


def get_clinton_tweets():
    my_file = Path('clintontwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('clintontwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@HillaryClinton', 'clintontwitters.pickle',
                        '796123724479164416')


def print_word_freqs(texts):
    texts = [s + ' ' for s in texts]
    str_copy = str(texts)
    # Get rid of punctuation
    word1 = " ".join(re.findall("[a-zA-Z]+",
                                str_copy))
    word1 = word1.split()
    stop_words = ['a', 't', 'co', 'https', 'to', 'in', 'n', 'is', 'nhttps']
    stop_words += ['the', 'and', 'amp', 'pm', 'out', 'on', 'for', 'at']
    stop_words += ['s', 'of', 'be', 'going', 'p', 'The', 'it', 'our']
    stop_words += ['Kz', 'jfd', 'this', 'that', 'TKJ', 'H', 'CXLD', 'will']
    stop_words += ['have', 'RT', 're', 'kz', 'If', 'This', 'with', 've']
    word1 = [word for word in word1 if word not in stop_words]
    my_dict = wordListToFreqDict(word1)
    sorted_words = sortFreqDict(my_dict)
    for val in sorted_words:
        print(val)


def retrieve_tweets(name, filename, idnum):

    api = twitter.Api(api_keys.consumer_key, api_keys.consumer_secret,
                      api_keys.access_token_key,
                      api_keys.access_token_secret)

    tweets = api.GetUserTimeline(screen_name=name, count=199, max_id=idnum)
    for status in tweets:
        print(status.id)
        print(status.created_at)
    tweets = [s.text for s in tweets]
    # Save data to a file
    f = open(filename, 'wb')
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
    aux = [(freqdict[key], key) for key in freqdict if freqdict[key] > 9]
    aux.sort()
    return aux


print("Hillary's Words: ")
print_word_freqs(get_clinton_tweets())
print("Trump's Words: ")
print_word_freqs(get_trump_tweets())
