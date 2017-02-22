import requests
import random

def trim_hamlet(string_input):
    beginning = string_input.find("ACT I.")
    ending = string_input.find("[Exeunt, bearing off the dead bodies")
    new_string = string_input[beginning : ending]
    return new_string

def process_hamlet(ham):
    ham = ham.replace("\n", " ")
    ham = ham.replace("--", " ")
    ham = ham.lower()
    ham = ham.split()
    return ham

def remove_punctuation(ham):
    char_names = ["fran.", "ber.", "mar.", "hor.", "king.", "cor.", "volt.",
        "laer.", "pol.", "queen.", "ham.", "oph.", "ghost.", "rey.", "ros.",
        "guil.", "pro.", "p.", "luc.", "all." "osr.", "[exeunt", "ii", "iii",
        "iv", "v", "capt.", "[enter", "gent.", "danes.", "1", "2", "clown.",
        "sirs.", "[exit.]"]
    index = 0
    for word in ham:
        ham[index] = word.strip(" ()[]-")
        if word in char_names:
            ham.remove(word)
            index = index - 1
        index += 1
    return ham

def histogram(wordlist):
    d = {}
    for item in wordlist:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d

def list_by_frequent(histogram):
    l = []
    for word in histogram:
        l.append((histogram[word], word))
    l.sort()
    return l[::-1]

def print_common(list, number = 10):
    h = 0
    while h < number:
        #print(list[h])
        h += 1

def random_hamlet(list, wordnum = 30):
    i = 0
    sentence = []
    while i < wordnum:
        sentence.append(random.choice(list))
        i += 1
    return " ".join(sentence)

def better_random(probdict, wordlist, wordnum = 30):
    i = 0
    sentence = [random.choice(wordlist).capitalize()]
    while i < wordnum - 1 or "." not in sentence[-1]:
        pos_list = probdict[sentence[-1].lower()]
        newword = random.choice(pos_list)
        if "." in sentence[-1] or "!" in sentence[-1] or "?" in sentence[-1]:
            newword = newword.capitalize()
        if newword in ["i", "i'll", "i;"]:
            newword = newword.capitalize()
        sentence.append(newword)
        i += 1
    return " ".join(sentence)

def even_better_random(probdict, tupdict, wordlist, wordnum = 30):
    i = 0
    det_rep = 0
    allow_rep = 3
    sentence = [random.choice(wordlist).capitalize()]
    while i < wordnum - 1 or "." not in sentence[-1]:
        if det_rep < allow_rep and i >= 2 and (sentence[-2], sentence[-1]) in tupdict:
            pos_list = tupdict[(sentence[-2].lower(), sentence[-1].lower())]
            #print(pos_list)
            if len(pos_list) == 1:
                det_rep += 1
                #print(det_rep)
            else:
                det_rep = 0
        else:
            pos_list = probdict[sentence[-1].lower()]
            if det_rep == allow_rep and len(pos_list) > 1:
                #print("Determinance broken.")
                det_rep = 0
        newword = random.choice(pos_list)
        if "." in sentence[-1] or "!" in sentence[-1] or "?" in sentence[-1]:
            newword = newword.capitalize()
        if newword in ["i", "i'll", "i;"]:
            newword = newword.capitalize()
        sentence.append(newword)
        i += 1
    return " ".join(sentence)

def prob_array(wordlist):
    d = {}
    index = 0
    for word in wordlist:
        if index == len(wordlist) - 1:
            break
        elif word not in d:
            d[word] = [wordlist[index + 1]]
        else:
            d[word].append(wordlist[index + 1])
        index += 1
    return d

def tuple_array(wordlist):
    d = {}
    index = 0
    while index < len(wordlist) - 3:
        tup = wordlist[index], wordlist[index + 1]
        if tup not in d:
            d[tup] = [wordlist[index + 2]]
        else:
            d[tup].append(wordlist[index + 2])
        index += 1
    return d

def test():
    hamlet_full = open("report.txt")
    ham = hamlet_full.read()
    #ham = trim_hamlet(ham)
    ham = process_hamlet(ham)
    ham = remove_punctuation(ham)
    return even_better_random(prob_array(ham), tuple_array(ham), ham, 60)
