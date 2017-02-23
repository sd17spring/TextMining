""" Analyzes and compares the word frequencies with Zipf's Law in
"The Trial" and "The Metamorphosis" by Franz Kafka
 downloaded from Project Gutenberg.

 Author: Onur, the Incompetent

"""

import string
import numpy
import matplotlib.pyplot as plt


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    refined_lines = []
    raw_list = ''
    while lines[curr_line].find('*** START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    while lines[curr_line].find('End of the Project Gutenberg EBook') == -1:
        refined_lines.append(lines[curr_line])
        curr_line += 1
    for i in range(0, len(refined_lines)):
        refined_lines[i] = refined_lines[i][0:len(refined_lines[i])-1]
        raw_list = " ".join(refined_lines)
    punc_table = " "*len(string.punctuation)
    punc_removed = raw_list.translate(str.maketrans(string.punctuation, punc_table))
    lowercase = punc_removed.lower()
    final_list = lowercase.split()
    return final_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """

    histogram = dict()
    for word in word_list:
        histogram[word] = histogram.get(word, 0)+1

    ordered_by_frequency = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    return(ordered_by_frequency[:100])


def zipf():
    x = []
    y = []
    dalist = get_top_n_words(word_list, 100)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(99):
        adding = dalist[i][1]
        x.append(i)
        y.append(adding)
    ax.set_title("Zipf's Law Analysis on 'The Metamorphosis'")
    ax.set_xlabel('Rank of the Word')
    ax.set_ylabel('Number of Times the Word is Used')
    ax.loglog(x, y)
    plt.plot(x, y)
    plt.savefig('ZipfMeta.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    word_list = get_word_list('metamorphosis.txt')
    print(get_top_n_words(word_list, 100))
    zipf()
