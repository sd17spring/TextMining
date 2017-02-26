"""
This is a self directional project with guidance from the Software Design
teaching team.

My project is focuesd around letter frequency in all words of the english
language compared to that of authors.

In addition, the same functions can be used to compare word choice (because of
letter frequencies) between two authors.

@author: Colvin Chapman

NLTK package:
    Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language
    Processing with Python. O’Reilly Media Inc.
    """
import nltk
import doctest
import pickle
import string
import math

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


def trim_string(st):
    """turns string into more managable format.
    >>> trim_string('SGHsdg.14!\n')
    'sghsdg'
        """
    st = st.upper()
    exclude = set(string.punctuation+string.digits+'\n'+'’ ‘ÉÈÀÂ“	”﻿')
    st = ''.join(ch for ch in st if ch not in exclude)
    return st


def trim_string_webster(st):
    """turns string into more managable format.
    >>> trim_string('SG Hsdg.14!\n')
    'SGH'
        """

    exclude = set(string.punctuation + string.digits + '\n' +
                  string.ascii_lowercase)
    st = ''.join(ch for ch in st if ch not in exclude)
    return st


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
    webster = trim_string_webster(websterfile.read())
    web_words = word(webster, 0, len(webster))
    web_word_list = word_entries(web_words)
    pickle_a_list('english_words_only', web_word_list)


def any_text(name_of_file):
    """Opens the text file,
    runs histogram
    returns dictionary of histogram"""
    of_file = open(name_of_file)
    s = trim_string(of_file.read())
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def word_choice(name_of_file):
    """Compiles letters in a string in order of most to least common letters
    used.
        """
    hist = any_text(name_of_file)
    couples = []
    end_string = ''
    for item in hist:
        couples.append((hist[item], item))
    couples.sort(key=lambda tup: tup[0])  # sorts in place
    coupless = couples[::-1]
    for pair in coupless:
        end_string += pair[1]
    return end_string


def levenshtein(s1, s2):
    """find out how similar
    the match is to other word_choice strings

    (taken from a reading journal)
            """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def histogram(wordstring):
    d = dict()
    for char in wordstring:
        d[char] = d.get(char, 0) + 1
    return d


def pickle_tester(file_name):
    """ Primariy for the dictionary which is stored as a list of words.
    returns a string in order of the most to least common characters.
        """
    english_file = open(file_name, 'rb')
    reloaded_english_words = pickle.load(english_file)

    hist = histogram(''.join(reloaded_english_words))
    couples = []
    end_string = ''
    for item in hist:
        couples.append((hist[item], item))
    couples.sort(key=lambda tup: tup[0])  # sorts in place
    coupless = couples[::-1]
    for pair in coupless:
        end_string += pair[1]
    return end_string


def norm(d1, d2):
    """takes in two dectionaries of frequency and returns a resultant vector
    representing how similar they are."""
    resultant_sum = 0
    total1 = 0
    total2 = 0
    for key in d1:
        total1 += d1[key]
        total2 += d2[key]
    for key in d1:
        resultant_sum += ((d1[key]/total1 - d2[key]/total2))**2
    return 100*resultant_sum**.5


def dict_resultant(filename):
    english_file = open('english_words_only.pickle', 'rb')
    reloaded_english_words = pickle.load(english_file)

    hist = histogram(''.join(reloaded_english_words))
    return norm(any_text(filename), hist)


print(norm(any_text('Oliver_Twist'), any_text('David_Copperfield')))
print(norm(any_text('Oliver_Twist'), any_text('Sherlock_Holmes')))

print(dict_resultant('Oliver_Twist'))

print(word_choice('Oliver_Twist'))
print(word_choice('David_Copperfield'))
print(word_choice('Sherlock_Holmes'))
print(word_choice('bible.txt'))

end_dict = 'EAISRTONCLPDMUHBGYFWVKJZXQ'
end_Oliver = 'ETAOINHRSDLUMWCGFYPBVKXJQZ'
end_David = 'ETAOINSHRDLMUWCYFGPBVKXJQZ'
end_Sherlock = 'ETAOINHSRDLUMWCYFGPBVKXJQZ'
end_Bible = 'ETHAONSIRDLUMFWCYGBPVKJZXQ'


print('Dict vs Oliver :   '   + str(levenshtein(end_dict, end_Oliver))+'\n' +
      str(dict_resultant('Oliver_Twist')))
print('Oliver vs David :   '  + str(levenshtein(end_Oliver, end_David))+'\n' +
      str(norm(any_text('Oliver_Twist'), any_text('David_Copperfield'))))
print('David vs Dict:   '     + str(levenshtein(end_David, end_dict))+'\n' +
      str(dict_resultant('David_Copperfield')))
print('Dict vs Sherlock:   '  + str(levenshtein(end_dict, end_Sherlock))+'\n' +
      str(dict_resultant('Sherlock_Holmes')))
print('Oliver vs Sherlock:   '+ str(levenshtein(end_Oliver, end_Sherlock)) +
      '\n' + str(norm(any_text('Oliver_Twist'), any_text('Sherlock_Holmes'))))
print('David vs Sherlock:   '+str(levenshtein(end_David, end_Sherlock))+'\n' +
      str(norm(any_text('Sherlock_Holmes'), any_text('David_Copperfield'))))
print('Bible vs Sherlock:   ' + str(levenshtein(end_Bible, end_Sherlock)) +
      '\n' + str(norm(any_text('bible.txt'), any_text('Sherlock_Holmes'))))
print('Dict vs Bible:   '     + str(levenshtein(end_David, end_Bible))+'\n' +
      str(dict_resultant('bible.txt')))
