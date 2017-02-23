import requests
import pickle
import string
import operator
import math
from os.path import exists
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob as tb


def save_book(book_name, link):
    '''saves text of book under book_name(stirng)
    from link(string) on project gutenberg'''
    f = open(book_name + '.pickle', 'wb')
    book_text = requests.get(link).text
    pickle.dump(book_text, f)
    f.close


def get_book(book_name):
    '''returns text of book saved under book_name(string).pickle'''
    file_name = book_name + '.pickle'
    if not exists(file_name):
        return 'book not saved'
    else:
        f = open(book_name + '.pickle', 'rb')
        text = pickle.load(f)
    return text


def save_and_get_book(book_name, link):
    '''combines save and get book functions (book_name is string)'''
    save_book(book_name, link)
    text = get_book(book_name)
    return text


def read(text):
    '''returns text(string) as list of the words with
    whitespace and punctuatio stripped'''
    text_read = []
    if not text == 'book not saved':
        word = ''
        start = 0
        for i in range(len(text)):
            if text[i] in string.whitespace:
                end = i
                word = text[start:end]
                text_read.append(word)
                start = i + 1
        return text_read
    else:
        print('wtf, not even a book')


# TODO strip the book text of stuff before/after

def word_frequency(word_list):
    '''takes in word_list(list) and returns dictionary
    with keys=words and values=frequencies'''
    d = dict()
    for w in word_list:
        frequency = d.get(w, 0)
        d[w] = frequency + 1
    return d


def sort_dict(d):
    '''takes in a dictionary and sorts by decreasing order of values'''
    sorted_dict = sorted(d.items(), reverse=True, key=operator.itemgetter(1))
    return sorted_dict


def top_x_words(x, sorted_dict):
    '''prints the x(int) most frequent words in sorted_dict(dictionary)
    sorted by most to least frequent words'''
    for w in sorted_dict[0:x]:
        print(w)


def analyze_sentiment(text):
    ''''''
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)


def analyze(book_name, link):
    ''''''
    save_book(book_name, link)
    text = get_book(book_name)
    read_text = read(text)
    frequency_dict = word_frequency(read_text)
    return frequency_dict


def find_tfidf(dict_list):
    '''finds tfidf from list of dictionaries'''
    res_list = []
    for d in dict_list:
        count = sum([d[i] for i in d.keys()])
        tfidf_dict = dict()
        for w in d.keys():
            # find tf
            tf = d[w]/count
            # find n containing
            n_containing = sum([1 for val in dict_list if w in val])
            # find idf
            idf = math.log(len(dict_list)/(n_containing))
            # tf*idf
            tfidf_dict[w] = tf*idf
        res_list.append(tfidf_dict)
    return res_list


def analyze_tfidf(dict_list):
    '''uses sorts and prints dict_list for TF-IDF dict'''
    sorted_dict_list = []
    for i, d in enumerate(dict_list):
        sorted_dict = sort_dict(d)
        sorted_dict_list = sorted_dict_list + sorted_dict
        print("document {}: ".format(i+1))
        for word, score in sorted_dict[:5]:
            print('\tWord: {}, TF-IDF: {}'.format(word, round(score, 5)))


dict_1 = analyze('pride_and_prejudice', 'http://www.gutenberg.org/files/1342/1342-0.txt')
dict_2 = analyze('sense_and_sensibility', 'http://www.gutenberg.org/cache/epub/161/pg161.txt')
dict_3 = analyze('emma', 'http://www.gutenberg.org/files/158/158-0.txt')
dict_4 = analyze('persuasion', 'http://www.gutenberg.org/cache/epub/105/pg105.txt')
dict_5 = analyze('study_in_scarlet', 'http://www.gutenberg.org/files/244/244-0.txt')
dict_6 = analyze('sign_of_four', 'http://www.gutenberg.org/cache/epub/2097/pg2097.txt')
dict_7 = analyze('adventures_of_sherlock', 'http://www.gutenberg.org/files/48320/48320-0.txt')
dict_8 = analyze('memiors_of_sherlock', 'http://www.gutenberg.org/files/834/834-0.txt')
# find_tfidf([pride_and_prejudice, study_in_scarlet])

dict_list = [dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7, dict_8]

# print(find_tfidf(dict_list))

tfidf_dicts = find_tfidf(dict_list)
analyze_tfidf(tfidf_dicts)

# for i, doc in enumerate(doc_list):
#     print("Top words in document {}".format(i + 1))
#     scores = {word: tfidf(word, doc, doc_list) for word in doc.words}
    # sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    # for word, score in sorted_words[:3]:
        # print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
