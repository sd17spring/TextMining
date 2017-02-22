import pickle
import string

input_file = open('beowulf_text.pickle', 'rb')
beowulf_reloaded = pickle.load(input_file)
beowulf_reloaded = beowulf_reloaded[607:-35540]
beowulf_mini = beowulf_reloaded[1000:2000]

input_file2 = open('aenid_text.pickle', 'rb')
aenid_reloaded = pickle.load(input_file2)
aenid_reloaded = aenid_reloaded[545:-19100]

text = 'Hello cruel world \n Why are people cruel \n I do not love the world'
prefix_length = 2


def process_file(text):
    hist = dict()
    prefixes_dict = dict()
    line_hangover = []
    for line in text.splitlines():
        line_hangover = process_line(line, hist, line_hangover)
    return hist


def process_line(line, hist, line_hangover):
    line = line.replace('-', ' ')
    line = line.replace("'", '')
    extended_line = line_hangover
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        if len(word) > 0:
            if word[0] not in string.digits:
                hist[word] = hist.get(word, 0) + 1
                extended_line.append(word)
    print(extended_line)
    return extended_line[-prefix_length:]


def process_prefixes(extended_line):
    pass


def different_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t


hist = process_file(text)
