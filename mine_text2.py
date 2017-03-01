from nltk import word_tokenize
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# koran.txt has koran excerpt manually copied and pasted from koran.pickle
with open('koran.txt', 'r') as myfile1:
    koran = myfile1.read().replace('\n', ' ')

# analyzing sentiment
analyzer = SentimentIntensityAnalyzer()
k_sent = analyzer.polarity_scores(koran)
print(k_sent)


def filter_text(text):
    '''
    This function removes all characters in a string that are not alpha
    or spaces. In addition, it handles the wrapping of words around the end
    of a line with by removing the '- '.
    '''
    text = text.lower()
    text = text.replace('- ', '')
    text_filtered = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz '
    for char in text:
        if char in alpha:
            text_filtered += char
    return text_filtered


def important_tokens(text):
    '''
    This function goes through text and creates a list of all words in the
    text that do not appear in the nltk stopwords list.
    '''
    stop = stopwords.words('english')
    tokens = [i for i in word_tokenize(text) if i not in stop]
    return tokens


def plot_most_common(tokens, n):
    '''
    This function uses Counter to find the n most common words in a list of
    words. It then plots a histogram of those words compared to their
    frequencies.
    '''
    letter_counts = Counter(tokens).most_common(n)
    words = []
    counts = []
    for word, count in letter_counts:
        words.append(word)
        counts.append(count)
    x_pos = np.arange(len(words))
    plt.bar(x_pos, counts, align='center')
    plt.xticks(x_pos, words)
    plt.show()


koran_filtered = filter_text(koran)
tokens = important_tokens(koran_filtered)
plot_most_common(tokens, 10)
