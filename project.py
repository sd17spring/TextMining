from bs4 import BeautifulSoup
import requests
import re
import pickle
import os.path
from pathlib import Path
import random

def dict_creation_one(script, things = dict()):
    '''Create the base dictionary; only to be called if there is no dicts.p already'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script:
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            newstring += (x)
    newstring = newstring.lower()
    listowords = newstring.split()
    index = 0
    for y in listowords:
        index += 1
        if index != len(listowords):
            if y not in entiredict:
                entiredict[y] = [listowords[index]]
            else:
                entiredict[y].append(listowords[index])
    return entiredict

def dict_creation_two(script, things = dict()):
    '''Create the base dictionary; only to be called if there is no dicts.p already'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script:
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            newstring += (x)
    newstring = newstring.lower()
    listowords = newstring.split()
    index = 0
    for x in range(0, len(listowords)-3):
        index = tuple((listowords[x], listowords[x+1]))
        if index not in entiredict:
            entiredict[index] = [listowords[x+2]]
        else:
            entiredict[index].append(listowords[x+2])
    return entiredict

def markov_chain_two(yup, yup2, allwordss):
    spech = random.randrange(300, 500)
    speech = []
    listowords = allwordss.split()
    speech.append(random.choice(listowords).lower())
    speech.append(random.choice(yup2[speech[0]]))
    speech[0] = speech[0].capitalize()
    print(speech)
    for i in range(2, spech-1):
        checker = (speech[i-2].lower(), speech[i-1].lower())
        if '.' in (speech[i-1]) or ('?' in (speech[i-1])) or ('!' in (speech[i-1])):
            speech.append(random.choice(yup[checker]).capitalize())
        else:
            appendix = random.choice(yup[checker])
            if appendix in "i'm i i'll i've":
                appendix = appendix.capitalize()
            speech.append(appendix)
    index = 0
    for x in speech:
        if "peter" in x.lower():
            speech[index] = "Trump"
        elif "lois" in x.lower():
            speech[index] = "Ivanka"
        elif "brian" in x.lower():
            speech[index] = "Pence"
        elif "stewie" in x.lower():
            speech[index] = "Obama"
        elif "quagmire" in x.lower():
            speech[index] = "ISIS"
        elif "meg" in x.lower():
            speech[index] = "Mexico"
        elif "chris" in x.lower():
            speech[index] = "China"
        elif "quahog" in x.lower():
            speech[index] = "MURICA"
        elif "griffin" in x.lower():
            speech[index] = "President"
        index += 1
    if ('.' in speech[-1]) or ('!' in speech[-1]) or ('?' in speech[-1]):
        product = ' '.join(speech)
    else:
        product = ' '.join(speech) + '.'
    return product

# html = BeautifulSoup(requests.get('http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=family-guy&episode=s01e01').text, 'lxml')
# thing = html.find("div", class_ = 'scrolling-script-container')
# # print(type(thing))
# # print(str(thing.text).replace('[', ']',))
# html.find('<div class="scrolling-script-container">')  # find the first paragraph
# str(html.find('<div class="scrolling-script-container">'))


if __name__ == '__main__':
    allscripts = ''
    my_file = Path("dict1.p")
    my_file2 = Path("dict2.p")
    my_file3 = Path("allwords.p")
    print(not my_file.is_file())
    print(not my_file2.is_file())
    print(not my_file3.is_file())
    if (not my_file.is_file()) or (not my_file2.is_file()) or (not my_file3.is_file()):
        basehtml = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=family-guy&episode=s'
        temptml = basehtml
        # for mini in ([8 '01e'], [22 '02e'], [23 '03e'], [28 '04e'], [19 '05e'], [13 '06e'], [17 '07e'], [22 '08e'], [19 '09e'], [24 '10e'], [23 '11e'], [22 '12e'], [19 '13e'], [21 '14e'], [14 '15e'])
        #     x = mini[0]
        #     y = mini[1]
        for i in range (1,8):   #season1
            temp =  temptml + '01e' + '0%d' % (i)
            html = BeautifulSoup(requests.get(temp).text, 'lxml')
            thing = html.find("div", class_ = 'scrolling-script-container')
            allscripts = allscripts + " " + str(thing.text)
        for i in range (1,22):   #season2
            if i < 10:
                temp =  temptml + '02e' + '0%d' % (i)
            else:
                temp =  temptml + '02e' + '%d' % (i)
            html = BeautifulSoup(requests.get(temp).text, 'lxml')
            thing = html.find("div", class_ = 'scrolling-script-container')
            allscripts = allscripts + " " + str(thing.text)

        for i in range (1,22):   #season3
            if i < 10:
                temp =  temptml + '02e' + '0%d' % (i)
            else:
                temp =  temptml + '02e' + '%d' % (i)
            html = BeautifulSoup(requests.get(temp).text, 'lxml')
            thing = html.find("div", class_ = 'scrolling-script-container')
            allscripts = allscripts + " " + str(thing.text)

        html = BeautifulSoup(requests.get('https://github.com/PedramNavid/trump_speeches/blob/master/data/full_speech.txt').text, 'lxml')
        thing = html.find("table", class_ = 'highlight tab-size js-file-line-container')
        allscripts += thing.text
        pickle.dump(allscripts, open("allwords.p", "wb"))
        pickle.dump(dict_creation_one(allscripts), open("dict1.p", "wb"))
        pickle.dump(dict_creation_two(allscripts), open("dict2.p", "wb"))
        pickle.dump(allscripts, open("backup.p", "wb"))

    attempt1 = pickle.load( open( "dict1.p", "rb"))
    attempt2 = pickle.load( open("dict2.p", "rb"))
    attempt3 = pickle.load( open("allwords.p", "rb"))
    #intro = str(input("Start with a word: "))
    #blah1 = markov_chain(attempt1)
    blah2 = markov_chain_two(attempt2, attempt1, attempt3)
    print(blah2)
