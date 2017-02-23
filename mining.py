import pickle
import wikipedia
import math
input_file = open('britentries.pickle', 'rb')
encyclopedia = pickle.load(input_file)





#finds index of next char
def find_next_char(i, string):
    while True:
        if string[i] == ' ' or string[i] == '\n':
            i += 1
        else:
            return i

#finds name of entry, must start with chars
def find_entry(i, string):
    entry = ''
    while True: #isolates entry titles
        if string[i] == '\n' or string[i:i+2] == '  ' or string[i:i+2] == '. ':
            break
        else:
            entry += string[i]
            i += 1
    return entry
#i_slice = find_next_char(i_slice) #determines index of first entry in table of contents



 #adds all entries to contents list
def fill_contents(i, string):
    contents = []
    while True:
        entry = find_entry(i, string)
        i += len(entry)
        if len(contents) > 1 and contents[0] == entry:
            break
        contents.append(entry)
        i = find_next_char(i, string)
    #contents = contents.sort()
    return contents

#checks if entry is name, if it is name, returns correct format, otherwise returns orgininal entry
def check_name(entry):
    comma = entry.find(',')
    if comma > - 1:
        entry = entry[comma+2:] + entry[:comma]
    return entry

#creates list of entries of texts
def fill_text_list(i, string, contents):
    texts = []
    for entry in contents:
        original = entry
        if entry.find('(') > -1:
            entry = entry[:entry.index('(') - 1]
        if len(entry) > 12:
            entry = entry[:12]
        if string.find(entry, i) >= 0:
            start = string.index(entry, i) + len(entry)
            end = string.index('\n\n', start)
            text = string[start:end]
            text.replace('\n', ' ')
            texts.append(text)
        else:
            contents.remove(original)
    return texts

def find_word(s):
    word = ''
    index = 0
    while True:
        if s[index] == ' ':
            return word
        else:
            word += s[index]
            index += 1

#returns alphabetically sorted list of words and their frequencies
def frequent_dict(s):
    d = dict()
    word_list = s.split()
    for word in word_list:
        word = word.strip('.')
        word = word.strip(',')
        word = word.strip('!')
        word = word.strip('?')
        word = word.lower()
        d[word] = d.get(word, 0) + 1
    tList = []
    for word in d:
        tList.append((word, d[word]))
    tList.sort()
    return tList

#needed for cosine similarity
def square_rooted(x):
    res = round(math.sqrt(sum([a*a for a in x])), 3)
    if res == 0:
        res == .001
    return res


def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    if denominator< .001 and denominator > -.001:
        return numerator/.001
    return numerator/denominator


def compare_texts(texts, contents, i): #returns cosine similarity of two texts
    entry = check_name(contents[i]) #makes name searchable on wikipedia
    wiki = wikipedia.page(entry)

    #texts of wiki and brit
    wiki_text = wiki.summary
    brit_text = texts[i]


    wiki_list = frequent_dict(wiki_text) #creates frewuency dict of wiki words
    wiki_words = [] # puts words in list
    for t in wiki_list:
        if t[1] == 0:
            del wiki_list[t[0]]
        else:
            wiki_words.append(t[0])

    brit_list = frequent_dict(brit_text)
    brit_words = []
    for t in brit_list:
        if t[1] == 0:
            del brit_list[t[0]]
        else:
            brit_words.append(t[0])


    brit_vector = []
    wiki_vector = []
    for i in range(len(wiki_words)): #creating the wiki and brit vectors
        if wiki_words[i] in brit_words:
            word = wiki_words[i]
            ib = brit_words.index(word)
            brit_vector.append(brit_list[ib][1])
            wiki_vector.append(wiki_list[i][1])
    print(i)
    return cosine_similarity(brit_vector, wiki_vector)

def make_compare_list(texts, contents):
    compare_list = []
    i = 0
    while True:
        try:
            wiki = wikipedia.page(contents[i])
            compare_list.append(compare_texts(texts, contents, i))
            i += 1
        except Exception:
            texts.remove(texts[i])
            contents.remove(contents[i])
        if i > (len(contents)-1) or i > (len(texts)-1):
            break
    return compare_list


i_slice = encyclopedia.index('ARTICLES IN THIS SLICE:') + len('ARTICLES IN THIS SLICE:')
i_slice += find_next_char(0, encyclopedia[i_slice:])
contents = fill_contents(0, encyclopedia[i_slice:])

texts = fill_text_list(encyclopedia.index(contents[0], encyclopedia.index(contents[0], i_slice +10)), encyclopedia, contents)

print(make_compare_list(texts, contents))
print(contents)
