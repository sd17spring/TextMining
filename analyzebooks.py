#!/usr/bin/python3
'''
    DESC: Creates database of Charles Dickens books and compares unknown books
    to database to determine whether or not Charles Dickens is the author
    AUTH: Connor Novak
    MAIL: connor.novak@students.olin.edu
    '''

import string
import operator
import numpy as np
import pdb

def get_word_list(file_name):
    '''
        DESC: Reads specified project Gutenberg book, strips header comments,
        punctuation, and whitespace, then returns lowercase list of words in book.
        ARGS:
        file_name - str - name of file where Gutenberk book text is stored
        RTRN: list of lowercase words in book
        '''
    book = open(file_name, 'r')
    lines = book.readlines()

    curr_line = 0
    # For every line that is before the start of the book, cut it out of lines
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    curr_line = len(lines)
    # For every line that is after the end of the book, cut it out of lines
    while lines[curr_line-1].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line -= 1
    lines = lines[:curr_line-1]

    # creates list of all words in all lines
    words = []
    for line in lines:
        line = line.replace('\u2019','')
        line = line.translate(str.maketrans('\u201c' + '\u201d' +string.punctuation,"                                  "))
        words.extend(line.split())

    # shifts words to all lowercase
    for word in range(len(words)):
        w = words[word]
        w = w.lower()
        words[word] = w

    return words


def get_top_n_words(word_list, n):
    """
        DESC: Returns n most frequently occurring words in a list of words
        ARGS:
        word_list - list - word list (assumed to all be in lower case with no
        punctuation)
        n - int - number of words to return (pass -1 to get all)
        RTRN: list of n most frequently occurring words ordered from most
        frequently to least frequently occurring
        """
    word_freq = {}
    for word in word_list:
        if (word in word_freq.keys()):
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    sorted_word_freq = sorted(word_freq.items(), key=operator.itemgetter(1))
    if(n == -1):
        return sorted_word_freq
    else:
        return sorted_word_freq[-n-1:-1]


def total_word_freq(booklist):
    """
        DESC: Generates word frequency list for all books in list
        ARGS:
        booklist - list - list of file names for books
        RTRN: word frequency list for all books
        """
    wordlist = []
    for book in booklist:
        print('MSG: checking file: '+book)
        wordlist.extend(get_word_list(book))
    wordfreq = get_top_n_words(wordlist,-1)
    return wordfreq


def average_text(booklist):
    """
        DESC: Averages text frequencies of books in list
        ARGS:
        booklist - list - list of file names for books to average
        RTRN: word frequency of the average book in the list
        """
    wordfreq = total_word_freq(booklist)
    for i in range(len(wordfreq)):
        wordfreq[i] = (wordfreq[i][0], wordfreq[i][1]/len(booklist))
    return wordfreq


def compare_texts(t1, t2):
    '''
        DESC: compares two lists of words by their cosine similarities
        ARGS:
        t1 - tuple list - first text's words and frequencies
        t2 - tuple list - second text's words and frequencies
        RTRN: cosine similarity of texts
        '''
    file = open('matrix.txt', 'w')
    # Creates list of words by frequency from all listed books
    book_list = ['oliver_twist.txt', 'bleak_house.txt', 'a_christmas_carol.txt',
     'great_expectations.txt', 'picture_of_dorian_gray.txt',
     'the_old_curiosity_shop.txt', 'pride_and_prejudice.txt']
    master_freq = total_word_freq(book_list)

    # Translates texts to matrices
    t1_mat = matricize(t1,master_freq)
    file.write(str(t1_mat)+'\n')
    t2_mat = matricize(t2,master_freq)
    file.write(str(t2_mat))
    ans = cos_sim(t1_mat,t2_mat)
    print('MSG: cosine similarity of text 1 and text 2: %d' % ans)
    file.close()
    return ans


def matricize(wordlist,master_list):
    '''
        DESC: converts word frequency list of tuples into a matrix for
        performing cosine similarity
        ARGS:
        wordlist - tuple list - words and frequencies of a text
        master_list - tuple list - words and frequencies to which to map values
        in wordlist
        RTRN: matrix of frequency of words in wordlist relative to master_list
        '''
    #pdb.set_trace()
    matrix = []
    for entry in range(len(master_list)): # for each word in master word list
        temp = 0 # temp var to check if number is put in matrix
        for entry2 in range(len(wordlist)): # for each word in wordlist

            # If the words match, add word frequency to that location in the
            # return matrix. Otherwise, add a 0
            if master_list[entry][0] == wordlist[entry2][0]:
                matrix.append(wordlist[entry2][1])
                temp = 1
                break

        if (temp == 0): matrix.append(0)
    return matrix


def cos_sim(m1,m2):
    '''
        DESC: determines the cosine similarity between two matrices
        ARGS:
        m1 - list - first matrix
        m2 - list - second matrix
        RTRN: float representing cosine similarity
        '''

    return np.dot(m1,m2) / (np.linalg.norm(m1)*np.linalg.norm(m2))


def main():
    '''
        DESC: Runs main analysis
        ARGS: none
        RTRN: none
        '''
    word_num = 10
    text1 = 'oliver_twist.txt'
    text2 = 'a_christmas_carol.txt'
    text3 = 'pride_and_prejudice.txt'

    freq1 = get_top_n_words(get_word_list(text1),word_num)
    print('MSG: got text1 list')
    freq2 = get_top_n_words(get_word_list(text2),word_num)
    print('MSG: got text2 list')
    freq3 = get_top_n_words(get_word_list(text3),word_num)

    print('MSG: comparing texts . . .')
    compare_texts(freq1,freq2)
    #compare_texts(freq1,freq3)
    #compare_texts(freq2,freq3)
    #print(cos_sim([0,0,0,0,0.5,0,0.2],[0,0,0,0,0.1,0,0.4]))


main()
