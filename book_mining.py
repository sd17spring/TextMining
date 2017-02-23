import requests
import pickle
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Save data to a file
def save_data(file_name, data):
    '''saves data of file_name with file_name type string'''
    f = open(file_name + '.pickle', 'wb')
    pickle.dump(data, f)
    f.close


def save_book(file_name, link):
    '''saves book from project gutenberg under file_name
    given link with file_name type string'''
    data = requests.get(link).text
    save_data(file_name, data)


# Load data from a file
def load_data(book_name):
    '''returns data of book_name.pickle, book_name is a string'''
    input_file = open(book_name + '.pickle', 'rb')
    text = pickle.load(input_file)
    return text


def read(book_name):
    '''reads file, break each line into words,
    strips whitespace and punctuation'''
    f = load_data(book_name)
    f_read = []

    for l in f.readlines():
        word = ''
        for c in l:
            if c not in string.whitespace:
                word = word + c
            else:
                if word != '':
                    f_read = f_read + [word.lower().strip()]
                    word = ''
    return f_read


def read_book(book_name):
    '''starts book at *** start and ends at *** end'''
    filename = book_name + '.pickle'
    book = read(filename)
    i = 0
    length = len(book)
    while i < length - 1:
        if (book[i] + book[i+1]) == '***start':
            book = book[i+2:len(book)]
            length = len(book)
        elif (book[i] + book[i+1]) == 'end***':
            book = book[0:i-1]
        else:
            book = book
        i = i + 1
    return book


def word_frequency(book_name):
    '''returns total number of words and frequency
    of every word'''
    book = read_book(book_name)
    d = dict()
    word_total = 0
    for w in book:
        frequency = d.get(w, 0)
        d[w] = frequency + 1
    for x in d:
        word_total = word_total + d[x]
    frequency_analysis = d, word_total
    return frequency_analysis


def sorted_frequency(book_text):
    '''sorts words by frequency, prints 20 most frequent'''
    frequency_analysis = word_frequency(book_text)
    # frequency_words is a dictionary with keys words
    # and values frequeny of word
    frequency_words = frequency_analysis[0]
    # sort
    for i in range(len(frequency_words)):
        for j in range(len(frequency_words)-1):
            if frequency_words[j][1] < frequency_words[j+1][1]:
                frequency_words[j][1], frequency_words[j+1][1] = frequency_words[j+1][1], frequency_words[j][1]
                print(frequency_words)

    # print
    # for i in range(20):
        # print(frequency_words[i][0])

    return frequency_words


def analyze_sentiment(book_name):
    ''''''
    book = read_book(book_name)
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_score(book)


# Grab data from project gutenberg
save_book('will_to_power_1_2', 'http://www.gutenberg.org/files/52914/52914-0.txt')
will_to_power_1_2 = load_data('will_to_power_1_2')
print(sorted_frequency(will_to_power_1_2))
