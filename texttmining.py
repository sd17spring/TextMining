import requests
import nltk
import pickle
from bs4 import BeautifulSoup

#Mary_Wade_text = requests.get('http://www.gutenberg.org/cache/epub/43585/pg43585.txt').text
#print(Mildred_Wirt_text)

# Save data to a file (will be part of your data fetching script)
# f = open('Mary_Wade_text.pickle', 'wb')
# pickle.dump(Mary_Wade_text, f)
# f.close()

#Load data from a file (will be part of your data processing script)
def get_pickle(file_name):
    input_file = open(file_name, 'rb')
    #input_file.seek(0)
    reloaded_copy_of_texts = pickle.load(input_file)
    reloaded_copy_of_texts = reloaded_copy_of_texts.split("END OF THIS PROJECT GUTENBERG EBOOK")
    return reloaded_copy_of_texts[0]
# #soup = BeautifulSoup(Wilkie_Collins_text, 'html.parser')
#print(soup.prettify())

def word_sectioning(s):
    """ Takes a string of words returns the first word

        s: a string
        returns: the first word
    >>> word_sectioning("I bat today")
    'I'
    >>> word_sectioning("I.ban")
    'I'
    """
    for index in range(0,len(s)):
        word_section = s[index]
        if  word_section == ' ' or word_section == '.' or  word_section == ',' or  word_section == '?' or  word_section == '!' or  word_section == ';' or  word_section == ':':
#        if  word_section == ' ':
            return s[:index]
    return s

def word_finder(s):
    """ Takes a string of words returns all of the words. Does not work if the
    sentence begings with a "stopper"

        s: a string
        returns: all of the word
    >>> word_sectioning(".I ran back. to the bat.I")
    'I', 'ran', 'back', 'to', 'the', 'bat', 'I'
    """
    index = 0
    word_start_stop_list = []
    s = ' ' + s
    while index+1 < len(s):
        if ((s[index] == ' ' or  s[index]== '.' or  s[index] == ',' or  s[index] == '?' or  s[index] == '!' or  s[index] == ';' or  s[index] == ':')
        and (s[index+1] != ' ' and  s[index+1] != '.' and  s[index+1] != ',' and  s[index+1] != '?' and  s[index+1] != ' !' and  s[index+1] != ';' and s[index+1] != ':')):
            full_word = word_sectioning(s[index+1:])
            word_start_stop_list.append(full_word)
            index = index + len(full_word)
        else:
            index = index +1
    #This words were take from the most common word list on Wikipedia
    stopwords = ['a', 'the', 'its', 'over', 'also', 'be', '"', 'to', 'of', 'and', 'in']
    stopwords += ['that', 'have', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'do', 'at']
    stopwords += ['this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she']
    stopwords += ['or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what']
    stopwords += ['so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when']
    stopwords += ['make', 'can', 'like', 'time', 'just', 'him', 'know', 'take', 'people']
    stopwords += ['And', 'are', 'said', 'had', 'says', 'you', 'was', 'I', 'is', 'The', 'were']
    stopwords += ['has', 'any', 'very', 'am', 'our', 'But', '\r\n', '\r\nAnd', '*', '\r\n\r\n', '\r\nThe']
    stopwords += ['[\r\n\r\n[Footnote', '\r\n\r\nHEG', '\r\n\r\nTHEU', '\r\n\r\nTRA',']\r\n\r\n[Footnote']

    final_word_list = [word for word in word_start_stop_list if word not in stopwords]
    return final_word_list
#    return word_start_stop_list

def word_frequency(s):
    """ Takes a string of words and using the word_finder program above returns
    how many times that word is used

        s: a string
        returns: number all words are used
    >>> word_sectioning(".I ran back. to the bat.I")
    'I': 2, 'the': 1, 'to': 1, 'bat': 1, 'ran': 1, 'back': 1
        """
    s = word_finder(s)
    d = dict()
    for c in s:
       d[c] = d.get(c, 0) + 1
    return d

#Not working because of items? and probably a problem with histogram which word finder was suppose to fix
def most_frequent(s):
    histo = word_frequency(s)
    my_list = []
    for x, f in histo.items():
        my_list.append((f, x))
    my_list.sort()

    sorted_list = []
    for f, x in my_list:
        sorted_list.append(x)
    return sorted_list[-20::]

#print(most_frequent(get_pickle('Wilkie_Collins_text.pickle')))
# reloaded_copy_of_texts = get_pickle('Maria_Stewart_text.pickle')
# print(reloaded_copy_of_texts)
