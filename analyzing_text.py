from gathering_text import get_trump_tweets, get_clinton_tweets
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


def print_word_freqs(texts):
    '''Prints the frequency of words used in the list texts'''
    texts = [s + ' ' for s in texts]
    str_copy = str(texts)
    # Get rid of punctuation
    text_letters = " ".join(re.findall("[a-zA-Z]+", str_copy))
    text_letters = text_letters.split()
    # Don't include words that tell you nothing
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
    # Get rid of stop words
    text_letters = [word for word in text_letters if word not in stop_words]
    my_dict = wordListToFreqDict(text_letters)
    sorted_words = sortFreqDict(my_dict)
    # Print the words sorted by frequency
    for val in sorted_words:
        print(val)


def wordListToFreqDict(wordlist):
    '''Given a list of words, return a dictionary of
     word-frequency pairs.'''
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


def sortFreqDict(freqdict):
    '''Sort a dictionary of word-frequency pairs in
    order of descending frequency.'''
    # Make list of dictionary entries as tuples
    # Include only words that show up more than 9 times
    freq_list = [(freqdict[key], key) for key in freqdict if freqdict[key] > 9]
    freq_list.sort()
    return freq_list


def main():
    '''Print Hillary and Trump's words and polarity scores'''
    print("Hillary's Words: ")
    print_word_freqs(get_clinton_tweets())
    print(analyzer.polarity_scores(str(get_clinton_tweets())))
    print("Trump's Words: ")
    print_word_freqs(get_trump_tweets())
    print(analyzer.polarity_scores(str(get_trump_tweets())))


if '__name__' == '__main__':
    main()
