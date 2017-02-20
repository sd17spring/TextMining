from gathering_text import get_trump_tweets, get_clinton_tweets
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


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


def main():
    print("Hillary's Words: ")
    print_word_freqs(get_clinton_tweets())
    print(analyzer.polarity_scores(str(get_clinton_tweets())))
    print("Trump's Words: ")
    print_word_freqs(get_trump_tweets())
    print(analyzer.polarity_scores(str(get_trump_tweets())))


if '__name__' == '__main__':
    main()
