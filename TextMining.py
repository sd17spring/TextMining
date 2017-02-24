"""
This is a self directional project with guidance from the Software Design
teaching team.

@author: Colvin Chapman

NLTK package:
    Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language
    Processing with Python. O’Reilly Media Inc.
    """
import nltk
import requests
import doctest
import pickle

# #nltk.download()
#
# unabridged_webster = requests.get(
#     'http://www.gutenberg.org/cache/epub/29765/pg29765.txt').text
#
# pickle.dump('Webster_Dictionary', unabridged_webster,)
#
# print(len(unabridged_webster))
# # print(unabridged_webster[0: 3000])


def word(webster_dict, start, end):
    """ Takes in a string with words in it, and returns a list of all the words
    in that string

    range: the area on the string that is used

    >>> word("I want to go", 1,12)
    ['want', 'to', 'go']
        """
    return nltk.word_tokenize(webster_dict[start: end])


def word_entries(word_list):
    """Takes on a list of words and returns only the words that are all
    capital letters.

    >>> word_entries(['adH', 'HAND', 'HAHA', 'UNiCoRN'])
    ['HAND', 'HAHA']
        """
    good_list = []
    for word in word_list:
        if len(word) > 2:
            if str.upper(word) == word:
                good_list.append(word)
    return good_list


def pickle_a_list(name, filey):
    """name: string that represents name of file"""

    item = open(name + '.pickle', 'wb')
    pickle.dump(filey, item)
    item.close()
    return


def pickle_test():
    """making sure the functions work before wasting time processig an entire
    dictionary

    It works!"""

    pickle_a_list('test_list', ['GAAA', 'BE', 'bsvavv'])

    test_pickle = open('test_list.pickle', 'rb')

    reloaded_test_pickle = pickle.load(test_pickle)
    return (reloaded_test_pickle)


def english_language():
    websterfile = open('Webster.txt')
    webster = websterfile.read()
    web_words = word(webster, 0, len(webster))
    web_word_list = word_entries(web_words)
    pickle_a_list('english_words', web_word_list)


def open_english():
    english_file = open('english_words.pickle', 'rb')
    reloaded_english_words = pickle.load(english_file)
    return reloaded_english_words


reloaded_english_words = open_english()
print(len(reloaded_english_words))

# doctest.run_docstring_examples(word, globals(), verbose=True)
