"""
This file does the word frequency analysis on any text that is passed
through the program
"""

import string
import doctest
from heapq import nlargest
from wordcloud import WordCloud


def count_words(text, stop_words=None):
    """
    Here is the count_words function, which counts the frequency of words. It
    is passed a text and all the words that are not supposed to be counted
    as part of the word frequency analysis.
    The unit test below both tests the accuracy of count_words and demonstrates
    that stop_words is being utilized correctly (and removing words like 'a'
    and 'is').

    input:  text is the string of text
            stop_words is all the extraneous words

    returns: a dictionary of words and their word counts

     >>> count_words('Java Java Java a', ['a', 'an'])
     {'java': 3}
     """

    # read the file and split into words
    words = text.split()

    # create dict with word count
    word_count = dict()
    for word in words:
        # remove digits from the word
        word = ''.join(c for c in word if not c.isdigit())
        # remove puctuation and whitespace
        word = word.strip(string.punctuation + string.whitespace)
        # convert the word to lowercase
        word = word.lower()
        # if stop word, skip
        if word == '' or word in stop_words:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count


def top50_cloud(dictionary, title, header):
    """
    prints top 50 words and generates word cloud

    input:  dictionary is the word frequency dict
            title is the name of the section
            header are the column titles
    """
    top50 = ''
    print('\n' + title)
    print('-' * len(title))
    print(header)
    for word in nlargest(50, dictionary, key=dictionary.get):
        print(word, dictionary[word], sep='\t')
        top50 = top50 + (word.replace('-', '') + ' ') * dictionary[word]

    wordcloud = WordCloud().generate(top50)
    image = wordcloud.to_image()
    image.show()

if __name__ == '__main__':
    doctest.testmod(verbose=True)
