import requests
import re
import pickle
import numpy as np
import matplotlib.pyplot as plt
import operator


def save_texts(link, filename):

    book_text = requests.get(link).text
    pickle.dump(book_text, open(filename, "wb"))


save_texts('http://www.gutenberg.org/files/98/98-0.txt', 'A_Tale_of_Two_Cities.txt')


def word_frequency(filename):



    file = open('words.txt', 'r')
    words = file.read().lower()
    file.close()
    file = open(filename, 'r')
    text = file.read().lower()
    length = len(words)
    words = words.split()

    dict = {}
    freq = []
    for i in words:
        dict[i] = text.count(i)
        count = text.count(i)
        freq.append(count)
    print(dict['the'])

    dict = sorted(dict.iteritems(), key=lambda (k, v): (v, k), reverse=True)
    dict = dict[:20]
    print(dict)

    wordlist = zip(*dict)[0]
    score = zip(*dict)[1]
    x_pos = np.arange(len(wordlist))
    x = range(0, 20)
    plt.bar(x_pos, score, align='center')
    #plt.plot(np.unique(x), np.poly1d(np.polyfit(x, score, 1))(np.unique(x)))
    plt.xticks(x_pos, wordlist)
    plt.ylabel('Frequency')
    plt.xlabel('Words')
    plt.title('Kama Sutra')
    plt.show()


word_frequency('Kama_Sutra.txt')
