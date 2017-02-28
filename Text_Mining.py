import requests
import pickle
import os.path
import nltk


"""Downloads 'Alice in Wonderland'
"""

# Save data to a file (will be part of your data fetching script)
if os.path.isfile('alice_in_wonderland.pickle') == False:
    alice_in_wonderland_full_text = requests.get('http://www.gutenberg.org/files/11/11-0.txt').text
    f = open('alice_in_wonderland.pickle', 'wb')
    pickle.dump(alice_in_wonderland_full_text, f)
    f.close()
else:
    # Load data from a file (will be part of your data processing script)
    input_file = open('alice_in_wonderland.pickle', 'rb')
    reloaded_copy_of_texts1 = pickle.load(input_file)


"""Downloads 'Tom Sawyer'"""

if os.path.isfile('tom_sawyer.pickle') == False:
    Tom_Sawyer_full_text = requests.get('http://www.gutenberg.org/files/74/74-0.txt').text
    f2 = open('tom_sawyer.pickle', 'wb')
    pickle.dump(Tom_Sawyer_full_text, f)
    f.close()
else:
    # Load data from a file (will be part of your data processing script)
    input_file2 = open('tom_sawyer.pickle', 'rb')
    reloaded_copy_of_texts2 = pickle.load(input_file2)

"""Cuts out beginning and end sections from each book"""

def cut_alice(text):
    index = text.find('***')
    new_text = text[index+3:]
    index2 = new_text.find('***')
    final_text = new_text[index2+3:]
    index3 = final_text.find('THE END')
    text3 = final_text[:index3+7]
    return text3


def cut_tom(text):
    index = text.find('Widger')
    final_text = text[index+6:]
    index2 = final_text.find('End of the Project')
    text3 = final_text[:index2-1]
    return text3


def parse_text(text):
    """Cuts the beginning and end off book to get just the actual text
    and removes spaces/punctuation. Also, changes all words to lowercase. Outputs
    a histogram with each word and the number of times it appears in the book.
    """
    tokens = nltk.word_tokenize(text)
    myDictionary = dict()
    for word in tokens:
        if word == "." or word == "," or word == "--" or word == ";" or word == ")" or word == "(" or word == "?" or word == "'" or word == "!" or word == ":" or word == "&":
            tokens.remove(word)
        elif word[0] == '_' and word[len(word)-1] == '_':
            word = word[1:len(word)-2]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        elif word[0] == '_':
            word = word[1:]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        elif word[len(word)-1] == '_':
            word = word[0:len(word)-1]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        elif word[len(word)-1] == "'":
            word = word[0:len(word)-1]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        elif word[len(word)-1] == ".":
            word = word[0:len(word)-1]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        elif word[len(word)-1] == ".'":
            word = word[0:len(word)-2]
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
        else:
            lword = word.lower()
            myDictionary[lword] = myDictionary.get(word,0) + 1
    return myDictionary


def most_frequent(hist1,hist2):
    """Takes histogram from both books and outputs 10 most common words from each that do
    not appear in the other book."""
    not_in_hist2 = []
    not_in_hist1 = []
    words1 =[]
    words2 =[]
    for number, word in hist1:
        words1.append(word)
    for number, word in hist2:
        words2.append(word)

    while len(not_in_hist2) <= 10:
        for value, word in hist1:
            if word not in words2:
                not_in_hist2.append((word,value))
    while len(not_in_hist1) <=10:
        for value, word in hist2:
            if word not in words1:
                not_in_hist1.append((word,value))
    return [len(not_in_hist1), not_in_hist1[0:14], len(not_in_hist2), not_in_hist2[0:14]]


def histogram_sort(hist):
    """Sorts histogram by common-ness of word and outputs the sorted list of
    tuples (number of appearances,word).
    """
    inverted = []
    for word,number in hist.items():
        inverted.append((number,word))
    inverted.sort(reverse = True)
    return inverted


def adventure(hist):
    """Outputs the number of times that the word adventure appears in the full text"""
    for value, word in hist:
        if word == 'adventure':
            return value
    return 0


def compare_texts(text1, text2):
    """Compares the two books and tells how similar they are. First, outputs
    percent of words for each that are unique. Then, outputs list
    of 15 most common words that appear in one but not the other.
    """
    text1_edit = histogram_sort(parse_text(text1))
    text2_edit = histogram_sort(parse_text(text2))
    data = most_frequent(text1_edit, text2_edit)
    percent_diff1 = (100*data[2])/len(text1_edit)
    percent_diff2 = (100*data[0])/len(text2_edit)
    adv1 = adventure(text1_edit)
    adv2 = adventure(text2_edit)

    text1_unique = data[3]
    text2_unique = data[1]

    output = "The first book is made up of %s percent unique words that are not found in book 2. The most common unique words found in book 1 are: %s. The second book is made up of %s percent unique words not found in book 1. The most common unique words in book 2 are: %s. Although both books have the word adventure in their titles, 'adventure' is only used %s times in book 1 and %s times in book 2.'"% (percent_diff1, text1_unique, percent_diff2, text2_unique, adv1, adv2)

    return output


text1 = cut_tom(reloaded_copy_of_texts2)
text2 = cut_alice(reloaded_copy_of_texts1)


print(compare_texts(text1,text2))
