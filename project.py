from bs4 import BeautifulSoup
import requests
import re
import pickle
import os.path
from pathlib import Path
import random

def dict_creation_one(script, things = dict()):
    '''Create the base dictionary for ONE word; only to be called if there is no dicts1.p already'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script: #get rid of symbols that I don't want in my speech
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            newstring += (x)
    newstring = newstring.lower()
    listowords = newstring.split()
    index = 0
    for y in listowords:    #run through all of the words and create a dictionary with them
        index += 1
        if index != len(listowords):
            if y not in entiredict:
                entiredict[y] = [listowords[index]]
            else:
                entiredict[y].append(listowords[index])
    return entiredict

def dict_creation_two(script, things = dict()):
    '''Create the base dictionary for TWO words; only to be called if there is no dicts.p already'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script: #get rid of symbols that I don't want in my speech
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            newstring += (x)
    newstring = newstring.lower()
    listowords = newstring.split()
    index = 0
    for x in range(0, len(listowords)-3): #run through all of the words and create a dictionary with them; the keys are tuples.
        index = tuple((listowords[x], listowords[x+1]))
        if index not in entiredict:
            entiredict[index] = [listowords[x+2]]
        else:
            entiredict[index].append(listowords[x+2])
    return entiredict

def markov_chain_two(yup, yup2, allwordss):
    """The markov chain function that actually generates the speech"""
    spech = random.randrange(300, 500) #generates a random speech of length randomly selected in this range
    speech = []
    listowords = allwordss.split()
    speech.append(random.choice(listowords).lower())
    speech.append(random.choice(yup2[speech[0]]))
    speech[0] = speech[0].capitalize()
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
    for x in speech:        #A variety of statements that change Family Guy specific phrases to those that Trump could use
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
        if '.' in x:
            temp = x
            mini = temp.split('.')
            speech[index] = mini[0]
            speech.insert(index, mini[1].capitalize())
        index += 1
    index = 0
    for y in speech:
        if " " in y:
            speech[index] = y.replace(' ', '')
        index += 1
    if ('.' in speech[-1]) or ('!' in speech[-1]) or ('?' in speech[-1]):   #how to determine if punctuation needs to be added at the end
        product = ' '.join(speech)
    else:
        product = ' '.join(speech) + '.'
    return product #return a string of the final speech.

if __name__ == '__main__':
    allscripts = ''
    my_file = Path("dict1.p")
    my_file2 = Path("dict2.p")
    my_file3 = Path("allwords.p")
    # print(not my_file.is_file()) #For testing purposes
    # print(not my_file2.is_file()) #For testing purposes
    # print(not my_file3.is_file()) #For testing purposes
    if (not my_file.is_file()) or (not my_file2.is_file()) or (not my_file3.is_file()): #check to see if there are already dictionaries; if there aren't then dictionaries are created.
        basehtml = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=family-guy&episode=s'
        temptml = basehtml
        # for mini in ([8 '01e'], [22 '02e'], [23 '03e'], [28 '04e'], [19 '05e'], [13 '06e'], [17 '07e'], [22 '08e'], [19 '09e'], [24 '10e'], [23 '11e'], [22 '12e'], [19 '13e'], [21 '14e'], [14 '15e'])
        #The above line is old code that I can reference to draw upon more family guy seasons
        for i in range (1,8):   #season1 of family guy
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

        #gather the trump speeches
        html = BeautifulSoup(requests.get('https://github.com/PedramNavid/trump_speeches/blob/master/data/full_speech.txt').text, 'lxml')
        thing = html.find("table", class_ = 'highlight tab-size js-file-line-container')
        allscripts += thing.text
        #pickle the necessary information
        pickle.dump(allscripts, open("allwords.p", "wb"))
        pickle.dump(dict_creation_one(allscripts), open("dict1.p", "wb"))
        pickle.dump(dict_creation_two(allscripts), open("dict2.p", "wb"))
        pickle.dump(allscripts, open("backup.p", "wb"))

    #call the dictionaries/all words to run the program with
    oneworddict = pickle.load( open( "dict1.p", "rb"))
    twoworddict = pickle.load( open("dict2.p", "rb"))
    allwords = pickle.load( open("allwords.p", "rb"))
    blah2 = markov_chain_two(twoworddict, oneworddict, allwords) #create the markov chain
    print(blah2) #print the markov chaing
