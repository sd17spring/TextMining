from collections import Counter
from bs4 import BeautifulSoup
import requests
import string
from numpy.random import choice

"""
Importing honor code
"""
html = BeautifulSoup(requests.get('http://www.olin.edu/academic-life/student-affairs-resources/student-life/honor-code/').text, 'lxml')
startpoint = html.get_text().find('The Olin Honor Code Values')
stoppoint = html.get_text().find('Quick Links')

honor = html.get_text()[startpoint:stoppoint]
listhonor = str(honor).split()

#print(listhonor)

"""
Importing felonies
"""
html = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Felony').text, 'lxml')
startpoint = html.get_text().find('Broadly, felonies')
stoppoint = html.get_text().find('are the least serious')

felonies = html.get_text()[startpoint:stoppoint]
listfelonies = str(felonies).split()

#print(felonies.replace('[',' ').replace(']', ' '))

"""
Import Olin Promotional Text
"""

html = BeautifulSoup(requests.get('http://www.olin.edu').text, 'lxml')
startpoint = html.get_text().find('At Olin')
stoppoint = html.get_text().find('institutions.')

promotion = html.get_text()[startpoint:stoppoint]
listpromotion = str(promotion).split()

#print(listpromotion)

"""
Combing felonies and honor into listhonor
"""

megalist = []
megalist.extend(listhonor)
megalist.extend(listfelonies)
megalist.extend(listpromotion)
#print(megalist)

#Finding word frequency
counts = Counter(megalist)
#print(counts)

"""Make dictionary
"""
def markov(megalist):


    i = 0;
    markovdict = {}
    for i in range(len(megalist)-1):
        if megalist[i] not in markovdict:
            markovdict[megalist[i]] = []
        markovdict[megalist[i]].append(megalist[i+1])
    return markovdict



def smushit(markovdict, megalist):

    finallist = []
    capitals = filter(lambda x: x.lower() != x, megalist)
    word = choice(list(capitals))
    finallist.append(word)
    while not word.endswith("."):
        word = choice(markovdict[word])
        finallist.append(word)
#        words = []
#        for k, v in next_word.items():
#            words.append(k)
    #         probs.append(v)
    #
    #     nxt = choice(words, p=probs)
    # finallist.append(nxt)
    return " ".join(finallist)

if __name__ == "__main__":
    x = markov(megalist)
    #print(x)
    print(smushit(x, megalist))
