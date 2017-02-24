import pickle
import nltk
import numpy
from nltk.tokenize import TweetTokenizer
import collections
books = ['odyssey', 'iliad','bible', 'cant', 'shakes', 'don', 'pride', 'frank', 'alice', 'sherlock', 'wilde']
unknown = 'suprise'

def openFile(name):
    pickledName = name + '.pickle'
    opened = open(pickledName, 'rb')
    txt = pickle.load(opened)
    txt = txt.lower()
    txt = txt.strip(',.?/1234567890~*()')
    return txt

def sortText(t):
    tknzr = TweetTokenizer()
    token = tknzr.tokenize(t)
    return token

def wordFreq(s):
    c = collections.Counter()
    for word in s:
        c[word] += 1
    return c

def makeWords():
    count = []
    dictionaries = []
    i = 0
    while i < len(books):
        sText = sortText(openFile(books[i]))
        words = wordFreq(sText)
        dictionaries.append(words)
        length = len(sText)
        count.append(length)
        i+=1
    return (dictionaries, count)

def fgivenWord(word, dictionaries, count, u, ulen):
    i = 0
    freq = []
    while i < len(dictionaries):
        bookDict = dictionaries[i]
        freqWord = bookDict[word]
        percent = freqWord/count[i]
        freq.append(percent)
        i += 1
    percentUnknown = u[word]/ulen
    return (freq, percentUnknown)

def allWords():
    u0 = sortText(openFile(unknown))
    u = wordFreq(u0)
    ulen = len(u0)

    dicts, counts = makeWords()

    distance = []
    for word in u.keys():
        f, k = fgivenWord(word, dicts, counts, u, ulen)
        array = numpy.array(f)
        diff = array - k
        distance.append(diff)
    mat = numpy.matrix(distance)
    interesting = numpy.mean(mat, axis = 0)
    return interesting


over = allWords().A1
a0 = numpy.array(over).tolist()

times = ['~ 800BC', '~ 800BC', '~100', '~1400', '~1600', '~1600', '~1810', '~1820', '~1860', '~1890', '~1900']
ind = a0.index(max(over))

print(times[ind])
print(over)
