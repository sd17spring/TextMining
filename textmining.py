# most common words
# this code computes the most common words of the adventure_of_sherlock_holmes
import pickle
import requests
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

adventure_of_sherlock_holmes = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
# Analyzing "Adventure of Sherlock Holmes"

# Save data to a file
f = open('adventure_of_sherlock_holmes.pickle', 'wb')
pickle.dump(adventure_of_sherlock_holmes, f)
f.close()

# Load data from a file
input_file = open('adventure_of_sherlock_holmes.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)
print(type(reloaded_copy_of_texts))


def process(s):
    # creates a dictionary called hist by stripping of the text
    hist = dict()
    new_s = s.replace('-', ' ')
    for word in new_s.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist


hist = process(reloaded_copy_of_texts)
print(hist)


def most_common(text):
    # creates the dictionary called t to find out most commonly used words
    t = []
    for key, value in text.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t


t = most_common(hist)
print('The most common words are:')
for freq, word in t[:10]:
    print(word, freq)
    # sort the dictionary by its values and returns
    # top 10 highest keys


def total_words(hist):
    return sum(hist.values())
    # return the total number of total words


def different_words(hist):
    return len(hist)
    # return the total number of different words


print('Total number of words:', total_words(hist))
print('Number of different words:', different_words(hist))


analyzer = SentimentIntensityAnalyzer()
print('Polarity Analyzer:')
print(analyzer.polarity_scores('adventure_of_sherlock_holmes.txt'))
# analyze the polarity of text by using SentimentIntesnityAnalyzer
