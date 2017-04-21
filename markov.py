from bs4 import BeautifulSoup
import requests
from numpy.random import choice


"""
Function that pulls text from web
"""
megalist = []
markovdict = {}
def words_from_internet(link='http://www.olin.edu/academic-life/student-affairs-resources/student-life/honor-code/', start='The Olin Honor Code Values', stop='Quick Links'):
    html = BeautifulSoup(requests.get(link).text, 'lxml')
    startpoint = html.get_text().find(start)
    stoppoint = html.get_text().find(stop)

    honor = html.get_text()[startpoint:stoppoint]
    listhonor = str(honor).split()

    # Combing all text into listhonor
    megalist.extend(listhonor)


"""
Make dictionary
"""


def markov(megalist):

    i = 0
    markovdict = {}
    for i in range(len(megalist)-1):
        if megalist[i] not in markovdict:
            markovdict[megalist[i]] = []
        markovdict[megalist[i]].append(megalist[i+1])
    # print(markovdict)
    return markovdict


def smushit(markovdict, megalist):

    finallist = []
    capitals = filter(lambda x: x.lower() != x, megalist)
    word = choice(list(capitals))
    finallist.append(word)
    print(markovdict[word])
    # while not word.endswith("."):
    #     word = choice(markovdict[word])
    #     print('foo')
    #     finallist.append(word)
    # return " ".join(finallist)


def main_important_part():
    words_from_internet(link='http://www.olin.edu/academic-life/student-affairs-resources/student-life/honor-code/',
                        start='The Olin Honor Code Values', stop='Quick Links')
    words_from_internet(link='https://en.wikipedia.org/wiki/Felony',
                        start='Broadly, felonies', stop='are the least serious')
    words_from_internet(link='http://www.olin.edu',
                        start='At Olin', stop='institutions.')
    # print(megalist)
    markov(megalist)
    smushit(markovdict, megalist)


if __name__ == "__main__":
    main_important_part()
