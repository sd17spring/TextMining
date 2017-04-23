"""
Mini Project 5--Re-editing of Mini Project 3 (Text Mining)
Author: Nicholas Sherman
Date: 4/22/2017
Class: Software Design

This project markov chains Family Guy scripts with Donald Trump speeches for entertainment purposes.
"""
from bs4 import BeautifulSoup
import requests
import re
import pickle
import os.path
from pathlib import Path
import random

def dict_creation_one(script, things = dict()):
    '''Create the base dictionary for ONE word; only to be called if there is no dicts1.p already.
    Basically, this is a one-off dictionary in order to determine the first words. It also allows
    for the possibility of more randomness at some point.
    inputs: a single string containing all scripts, a dictionary can be overloaded to help shorten the creation time of the dictionary
    outputs: a dictionary of one word keys for markov chaining'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script: #get rid of symbols that I don't want in my speech
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            newstring += (x)
    newstring = newstring.lower()
    listowords = newstring.split()
    index = 0
    for y in listowords:    #run through all of the words in the speech and create a dictionary with them; this is a single word dictionary
        index += 1
        if index != len(listowords):
            if y not in entiredict:
                entiredict[y] = [listowords[index]]
            else:
                entiredict[y].append(listowords[index])
    return entiredict

def dict_creation_two(script, things = dict()):
    '''Create the base dictionary for TWO words; only to be called if there is no dicts.p already.
    This is the dictionary that is referenced for most of the project.
    inputs: a single string containing all scripts, a dictionary can be overloaded to help shorten the creation time of the dictionary
    outputs: a dictionary with two word keys for markov chaining'''
    entiredict =  things
    everything = script
    newstring = ''
    for x in script: #get rid of symbols that I don't want in my speech
        if x not in ('[', ']', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '"', '\\', '—', '|', '-'):
            if x in ('!', '.', '?'):
                newstring += (x)
            else:
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
    """The markov chain function that actually generates the speech
    inputs: a two key-word dictionary, a one key-word dictionary, and a string of all scripts
    outputs: a string that is the "final" speech that Trump would make"""
    spech = random.randrange(300, 500) #generates a random speech of length randomly selected in this range (in words)
    speech = []
    listowords = allwordss.split()
    speech.append(random.choice(listowords).lower())
    speech.append(random.choice(yup2[speech[0]]))
    speech[0] = speech[0].capitalize()
    for i in range(2, spech-1):     #Make a speech of length spech through referencing the dictionaries yup and yup2
        checker = (speech[i-2].lower(), speech[i-1].lower())
        if '.' in (speech[i-1]) or ('?' in (speech[i-1])) or ('!' in (speech[i-1])):
            speech.append(random.choice(yup[checker]).capitalize())
        else:
            appendix = random.choice(yup[checker])
            if appendix in "i'm i i'll i've":   #capitalize I
                appendix = appendix.capitalize()
            speech.append(appendix)
    index = 0
    for x in speech:        #A variety of statements that change Family Guy specific phrases to those that Trump could use
        xl = x.lower()
        if "peter" in xl:
            speech[index] = "Trump"
        elif "lois" in xl:
            speech[index] = "Ivanka"
        elif "brian" in xl:
            speech[index] = "Pence"
        elif "stewie" in xl:
            speech[index] = "Obama"
        elif "quagmire" in xl:
            speech[index] = "ISIS"
        elif "meg" in xl:
            speech[index] = "Mexico"
        elif "chris" in xl:
            speech[index] = "China"
        elif "quahog" in xl:
            speech[index] = "MURICA"        #This is more likely to sound like Trump than "America"
        elif "griffin" in xl:
            speech[index] = "President"
        if '.' in x:
            temp = x
            mini = temp.split('.')
            speech[index] = mini[0]
            speech.insert(index, mini[1].capitalize())
        index += 1
    index = 0
    for y in speech:    #Fixes some of the spacing issues
        if " " in y:
            speech[index] = y.replace(' ', '')
        index += 1
    if ('.' in speech[-1]) or ('!' in speech[-1]) or ('?' in speech[-1]):   #how to determine if punctuation needs to be added at the end
        product = ' '.join(speech)
    else:
        product = ' '.join(speech) + '.'
    product = product.replace('  ', ' ')        #replace all double spaces with single spaces.
    return product

if __name__ == '__main__':
    max_season = 3
    allscripts = ''
    my_file = Path("dict1.p")
    my_file2 = Path("dict2.p")
    my_file3 = Path("allwords.p")
    remake = False
    y = input("Do you want to customize the number of seasons? (y/n)")
    if y.lower() == 'y':
        max_seasons = input("How many seasons do you want?: ")
        remake = True
    # print(not my_file.is_file()) #For testing purposes
    # print(not my_file2.is_file()) #For testing purposes
    # print(not my_file3.is_file()) #For testing purposes
    if (not my_file.is_file()) or (not my_file2.is_file()) or (not my_file3.is_file()) or remake: #check to see if there are already dictionaries; if there aren't then dictionaries are created.
        basehtml = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=family-guy&episode=s'
        temptml = basehtml
        episodes_in_season = [-1, 8, 22, 23, 28, 19, 13, 17, 22, 19, 24, 23, 22, 19, 21, 14]
        for season in range (1, max_season):
            for i in range (1,episodes_in_season[season]):   #rewritten for all seasons; writes the link in a way to grab the seasons correctly
                if season < 10:
                    if i < 10:
                        temp =  temptml + '0%de' % season + '0%d' % (i)
                    else:
                        temp =  temptml + '0%de' % season + '%d' % (i)
                else:
                    if i < 10:
                        temp =  temptml + '%de' % season + '0%d' % (i)
                    else:
                        temp =  temptml + '%de' % season + '%d' % (i)
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
    print(blah2) #print the markov chaining
