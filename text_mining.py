"""
NAME: Prava

This program is the main program for the text_mining project. It takes all
the inaugural addresses and generates a list of the top words in total and
the words that are used across the most speeches. Then, a word cloud is
generated for both.
"""

import os
from text_analysis import count_words, top50_cloud

# stop words
f = open('/home/prava/TextMining/stopwords.txt')
# read the file and get stop words
stop_words = f.read().split()
f.close()

# text files path
path = '/home/prava/TextMining/textfiles/'
# file names
files = next(os.walk(path))[2]

count = []

for file in files:
    # open the file
    f = open(path + file)
    count.append(count_words(f.read(), stop_words))


# create a dict for counting words in all documents
count_all = dict()
for word_count in count:
    for word in word_count:
        if word not in count_all:
            count_all[word] = word_count[word]
        else:
            count_all[word] += word_count[word]


# shows the top 50 words from all the documents together
top50_cloud(count_all, 'Words used most in all texts together', 'WORD\tCOUNT')


# create a dict for counting words and number of documents
count_doc = dict()
for word in count_all:
    count_doc[word] = 0
    for word_count in count:
        if word in word_count:
            count_doc[word] += 1


# shows the top 50 words that appear in the most number of documents
top50_cloud(count_doc, 'Words used in most texts', 'WORD\tDOCUMENTS')
