import pickle
import string

input_file = open('beowulf_text.pickle', 'rb')
beowulf_reloaded = pickle.load(input_file)
beowulf_reloaded = beowulf_reloaded[607:-35540]
beowulf_mini = beowulf_reloaded[1000:2000]

input_file2 = open('aenid_text.pickle', 'rb')
aenid_reloaded = pickle.load(input_file2)
aenid_reloaded = aenid_reloaded[545:-19100]


def process_file(filename):
    hist = dict()
    text = open(filename)
    for line in text:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')
    line = line.replace("'" '')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def different_words(hist):
    return len(hist)


hist = process_file(beowulf_mini)
'''the issue is that beowulf_mini isn't a file name, it's a string. a very long
string. not sure how to fix that.'''

print(different_words(hist))
