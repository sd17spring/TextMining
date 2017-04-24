import pickle
import nltk
import numpy
from nltk.tokenize import TweetTokenizer
import collections


class bookDater():
    def __init__(self):
        #list names of pickled books and corresponding dates from project gutenburg
        self.books = ['odyssey', 'iliad','bible', 'cant', 'shakes', 'don', 'pride', 'frank', 'alice', 'sherlock', 'wilde']
        self.times = ['~ 800BC', '~ 800BC', '~100', '~1400', '~1600', '~1600', '~1810', '~1820', '~1860', '~1890', '~1900']
        #name of book that program is guessing age
        self.unknown = 'suprise'
        #finds distance between books given word count and flatens into a 1xn list of values
        self.over = numpy.absolute(self.allWords().A1)
        self.a0 = numpy.array(self.over).tolist()
        #finds the minimum difference between books
        self.ind = self.a0.index(min(self.over))
        #prints estimated publication date and differnces
        print(self.times[self.ind])
        print(self.over)

    def makeWords(self):
        #makes a dictionary of all of the dictioaries of word frequencies of each book
        #also returns number of words in each book in 'count' variable
        count = []
        dictionaries = []
        i = 0
        while i < len(self.books):
            p = processText()
            sText = p.tokenizeText(p.openFile(self.books[i]))
            words = p.wordFreq(sText)
            dictionaries.append(words)
            length = len(sText)
            count.append(length)
            i+=1
        return (dictionaries, count)

    def fgivenWord(self, word, dictionaries, count, u, ulen):
        #calculates percentage of each book that is made up of each word
        i = 0
        freq = []
        while i < len(dictionaries):
            bookDict = dictionaries[i]
            freqWord = bookDict[word]
            percent = freqWord/count[i]
            freq.append(percent)
            i += 1
        #tells how much of the unknown book is made up of each word
        percentUnknown = u[word]/ulen
        return (freq, percentUnknown)

    def allWords(self):
        #opens and tokenizes unknown text and determines word frequency
        p = processText()
        u0 = p.tokenizeText(p.openFile(self.unknown))
        u = p.wordFreq(u0)
        ulen = len(u0)

        dicts, counts = self.makeWords()

        distance = []
        for word in u.keys():
            f, k = self.fgivenWord(word, dicts, counts, u, ulen)
            array = numpy.array(f)
            diff = array - k
            distance.append(diff)
        mat = numpy.matrix(distance)
        interesting = numpy.mean(mat, axis = 0)
        return interesting

class processText():
    #basic word processing
    def openFile(self, name):
        #opens each pickled file, removes nonalphabetic characters and makes all words lowercase.
        pickledName = name + '.pickle'
        opened = open(pickledName, 'rb')
        txt = pickle.load(opened)
        txt = txt.lower()
        txt = txt.strip(',.?/1234567890~*()')
        return txt

    def tokenizeText(self, t):
        #tokenizes text such that each word is its own element in a list
        tknzr = TweetTokenizer()
        token = tknzr.tokenize(t)
        return token

    def wordFreq(self, s):
        #lists the frequency of each word in the book in a dictionary
        c = collections.Counter()
        for word in s:
            c[word] += 1
        return c


if __name__ == '__main__':
    bookDater()
