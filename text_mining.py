"""
SoftDes project 3: text mining

Noah Rivkin

use text mining and markov chains to generate text based on silly
book/movie/comic villain monologues....

or if I cannot find a large sample size imitate Shakespeare
"""

import requests
import re
import pickle
import random
import os
import string


suffix_dict_dict = {}


def get_text(file_name, url = ''):
    """
    opens the file with text in it, if the file exists.
    If the file does not exist gets the text from the web adress, and
    stores it in a pickled format,before opening it to read
    for example http://www.gutenberg.org/cache/epub/100/pg100.txt,
    which is the complete works of Shakespeare
    """
    if os.path.exists(file_name): # checks if the file has already been downloaded
        f = open(file_name, 'rb')
        text = pickle.load(f)
        f.close
        return text[900: len(text)]
    else:
        text = requests.get(url).text
        f = open(file_name, 'wb')
        pickle.dump(text, f)
        f.close
        return text[900: len(text)]


# def histogram(text):
#     """
#     generates dictionary with word frequencies
# 
#     This function is not used in the main program, and was created for testing purposes
# 
#     >>> histogram('d d d d d')
#     {'d': 5}
#     """
#     hist = {}
#     text = text.replace('\r','\r ') # keeps the return, but still splits up the words
#     text = text.split(' ')
#     for word in text:
#         word = word.strip(string.punctuation + string.whitespace + '1234567890?')
#         word = word.lower()
#         if word not in hist and word != '':
#             hist[word] = 1
#         elif word != '':
#             hist[word] = hist[word] + 1
#     return hist
# 
# 
# def get_most_freq(hist, n):
#     """
#     finds the n most common words
# 
#     This function is not used in the main program, and was created for testing purposes
# 
#     >>> get_most_freq({'a': 5, 's': 3, 'd': 7},2)
#     [['d', 'a'], [7, 5]]
#     """
#     top_n_words = []
#     top_n_freqs = []
#     for i in range(n):
#         most_common = ''
#         most_times = 0
#         total = 0
#         for key in hist:
#             if key not in top_n_words:
#                 num = hist[key]
#                 if num > most_times:
#                     most_times = num
#                     most_common = key
#         top_n_words.append(most_common)
#         top_n_freqs.append(most_times)
#     return [top_n_words, top_n_freqs]


def get_random_word(hist):
    """
    gets a random word from a dictionary of word frequencies, wieghted by frequency
    """
    total_words = 0
    for word in hist:
        total_words += hist[word]
    rand_num = random.randint(0,total_words)
    count = 0
    default = '...'
    for word in hist:
        if count >= rand_num: # to deal with incrementing from 0
            return word
        else:
            default = word
            count += hist[word]
    return default # avoids errors that can crop up


def get_suffix_dict(text, prefix):
    """
    generates a histogram for words following a prefix
    """
    if prefix in suffix_dict_dict:
        return suffix_dict_dict[prefix]
    else:
        suffix_hist = {}
        # text = text.replace('\r',' ')
        # text = text.split(' ')
        # null = ''
        # while null in text:
        #     text.remove(null)
        prefix = prefix.strip('1234567890' + '()\"\r\v\f-')
        comp_prefix = prefix.split('\t') # splits the prefix into a list for easy manipulation
        for i in range(len(text) - 1):
            text[i] = text[i].strip('1234567890' + '()\"\r\t\v\f-')
            if i > 2:
                test_prefix = [text[i - 1], text[i - 2]]
                suffix = text[i]
                if test_prefix == comp_prefix:
                    if suffix not in suffix_hist:
                        suffix_hist[suffix] = 1
                    else:
                        suffix_hist[text[i]] += 1
        suffix_dict_dict[prefix] = suffix_hist
        return suffix_hist


def gen_chain(seed1, seed2, length, text):
    """
    creates Markov chain
    """
    text = text.replace('\r','\r ')
    text = text.split(' ')
    null = ''
    while null in text:
        text.remove(null)
    chain = []
    for i in range(length):
        chain.append(seed1)
        prefix = seed2 + '\t' + seed1
        seed1 = seed2
        seed2 = get_random_word(get_suffix_dict(text, prefix))
    return chain


def markovchain(seed1, seed2, length, text):
    """
    this for my convenience
    """
    chain = gen_chain(seed1, seed2, length, text)
    result = ''
    for word in chain:
        result = result + word + ' '
    return result


text = get_text('war_and_peace.txt')


print(markovchain('it', 'was', 100, text))


import doctest
doctest.testmod()