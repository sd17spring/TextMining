"""
Software Design Project 3
Analyzing writing style in the Inheritance Cycle
Anil Patel

This project will be attempting to perform a variety of linguistic analyses on
two books in the Inheritrance Cycle - Eragon, the first book, and Inheritance,
the last book. I'm curious about the differences or similarities that might
exist because the first book was written when the author was 15 years old and
the last when he was 23.
"""

# Import some stuff
import nltk

# Setup books as lists with NLTK

# Open Eragon sample into a list of words
f = open("eragon_full.txt", "r")            # Open txt file
eragon = f.read()                           # Convert into workable variable
list_eragon = nltk.word_tokenize(eragon)    # Use NLTK to tokenize the text
# print(list_eragon)                        # Test above line by printing


# Do the same with inheritance sample
g = open("inheritance_full.txt", "r")
inheritance = g.read()
list_inheritance = nltk.word_tokenize(inheritance)
# print(list_inheritance)


def fix_txt(some_list):
    """
    Function to separate word from random characters and end of sentence
    punctuation that is misprinted in the txt file or parsed incorrectly by
    NLTK

    Separates end of sentence punctuation accidentally included in word strings
    by NLTK so that I can analyze sentence lengths later.

    >>> fix_txt([".share//"])
    ['.', 'share']
    """

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence_end = ".?!"
    thing = []

    for word in some_list:
        new_word = ""
        for i in range(0, len(word)):
            if word[i] in alphabet:
                new_word = new_word + word[i]
            if word[i] in sentence_end:
                thing.append(word[i])
        if len(new_word) > 0:
            thing.append(new_word)

    return(thing)


def shrink_list(some_list):
    """
    removes all words less than 4 letters from a list

    >>> shrink_list(["the", "nothing"])
    ['nothing']
    """
    # print(some_list)  # print initial list
    updated = []        # initialize a new list to add to

    for word in some_list:
        if len(word) > 3:
            updated.append(word)

    return updated


def average_word_length(some_list):
    """
    Function that will take a list of words and return the average word
    length for the list. First uses fix_txt and shrink_list to modify list.

    >>> average_word_length(["long", "else", "shot"])
    4.0
    """
    some_list = fix_txt(some_list)              # clean up list
    some_list = shrink_list(some_list)          # remove words < 3 letters
    sum_letters = 0                             # initialize a sum variable

    for word in some_list:                      # run through the list
        letters = len(word)                     # grab length of word
        sum_letters = sum_letters + letters     # update sum

    average = sum_letters / len(some_list)      # define average
    average = round(average, 3)
    return average


def word_frequency(s):
    """
    Modify the histogram function from the reading journal to determine the
    frequency of words in a list. Takes in a list instead of a string and
    counts frequency of words instead of letters.

    Will do some comparative testing with more functions eventually
    """

    s = fix_txt(s)          # Fix the list
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)+1
    return d


def sentence_length(some_list):
    """
    Figure out the average length of 1 sentence in each text.
    """

    # String of all end sentence punctuation
    end_sentences = ".?!"

    # Initialize list of end sentence indices
    ends = []

    # Initialize list of sentence lengths
    lengths = []

    # Clean up list for analysis
    some_list = fix_txt(some_list)

    # Run through list and index all sentence ends
    for i in range(0, len(some_list)):
        if some_list[i] in end_sentences:
            ends.append(i)

    # Run through list of ends and get # of words per sentence
    for i in range(0, (len(ends)-1)):
        sen_length = ends[i+1] - ends[i]
        lengths.append(sen_length)

    # Run through list of lengths and add up numbers
    total_words = 0
    for length in lengths:
        total_words = total_words + length

    # Grab averages
    average1 = total_words / len(lengths)
    average1 = round(average1, 3)
    # Alternate, faster method of computing the average
    # average2 = len(some_list) / len(ends)

    return average1


eragon_sen = sentence_length(list_eragon)
inheritance_sen = sentence_length(list_inheritance)

word_eragon = (average_word_length(list_eragon))
word_inheritance = (average_word_length(list_inheritance))

print(eragon_sen)
print(inheritance_sen)
print(word_eragon)
print(word_inheritance)


if __name__ == "__main__":
    import doctest
doctest.testmod()

# print(word_frequency(list_eragon))
