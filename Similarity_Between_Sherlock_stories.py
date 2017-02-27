"""
This program calculates the cosine similarity of all Sherlock Holmes books written
by Sir. Arthur Connan Doyle and the first book in the series, A Study In Scarlet.
It graphs the cosine similarity against time to investiage the evolution of
Doyle's writing.


Author: MJ-McMillen
"""
from __future__ import division
import requests #used to get books from guttenberg
import math
#used to plot
import numpy as np
import matplotlib.pyplot as plt
import wikipedia


#A_Study_In_Scarlet = requests.get('http://www.gutenberg.org/ebooks/244.txt.utf-8').text
A_Study_In_Scarlet= open('astudyinscarlet.txt.utf-8')
A_Study_In_Scarlet_lines = A_Study_In_Scarlet.readlines()
full_Study = A_Study_In_Scarlet_lines[63:4713]

#A_Sign_Of_Four = requests.get('http://www.gutenberg.org/ebooks/2097.txt.utf-8').text
A_Sign_Of_Four= open('A_Sign_Of_Four.txt.utf-8')
A_Sign_Of_Four_lines = A_Sign_Of_Four.readlines()
full_Sugn = A_Sign_Of_Four_lines[34:4576]

#Box = requests.get('http://www.gutenberg.org/ebooks/2344.txt.utf-8').text
Box= open('cardboardbox.txt.utf-8')
Box_lines = Box.readlines()
full_Box = Box_lines[35:905]

#Bow = requests.get('http://www.gutenberg.org/ebooks/2350.txt.utf-8').text
Bow= open('last_bow.txt.utf-8')
Bow_lines = Bow.readlines()
full_bow = Bow_lines[36:776]

#Lodge = requests.get('http://www.gutenberg.org/ebooks/2343.txt.utf-8').text
Lodge= open('wisterialodge.txt.utf-8')
Lodge_lines = Lodge.readlines()
full_Lodge = Lodge_lines[35:1329]

#Hound = requests.get('http://www.gutenberg.org/ebooks/2852-0.txt.utf-8').text
Hound= open('The_Hound.txt.utf-8')
Hound_lines = Hound.readlines()
full_Hound = Hound_lines[32:6859]

#The_valley = requests.get('http://www.gutenberg.org/ebooks/3289.txt.utf-8').text
The_valley= open('the_valley_of_fear.txt.utf-8')
The_valley_lines = The_valley.readlines()
full_valley = The_valley_lines[32:6801]

#The_Dying = requests.get('http://www.gutenberg.org/ebooks/2347.txt.utf-8').text
The_Dying= open('The_Dying_Detective.txt.utf-8')
The_Dying_lines = The_Dying.readlines()
full_Dying = The_valley_lines[36:778]

#Memoirs_get = requests.get('http://www.gutenberg.org/ebooks/834.txt.utf-8').text
Memoirs_get= open('memoirs_of_sherlock_holmes.txt.utf-8')
full_memoir =  Memoirs_get.readlines()
AMT = ["The Silver Blaze","The Yellow Face",
       "The Stock-Broker's Clerk","The Gloria Scott",
       "The Musgrave Ritual","The Renigate Puzzle",
       "The Crooked Man","The Resident Patient",
       "The Greek Interpreter","The Naval Treaty",
       "The Final Problem"]
AMB = [full_memoir[32:1121], full_memoir[1121:1902], full_memoir[1902:2714], full_memoir[2714:3521],
        full_memoir[3521:4311], full_memoir[4311:5160],full_memoir[5160:5895],full_memoir[5895:6764],
        full_memoir[6764:7572], full_memoir[7572:9103],full_memoir[9103:9857]]
Memoirs = {}
for i in AMT:
    Memoirs[i] = AMB[AMT.index(i)]

#Return_get = requests.get('http://www.gutenberg.org/ebooks/108.txt.utf-8').text
Return_get = open('the_return_of_sherlock_holmes.txt.utf-8')
full_return = Return_get.readlines()
ART = ["The Adventure Of The Empty House","The Adventure Of The Norwood Builder",
       "The Adventure Of The Dancing Men","The Adventure Of The Solitary Cyclist",
       "The Adventure Of The Priory School","The Adventure Of Black Peter",
       "The Adventure Of Charles Augustus Milverton","The Adventure Of The Six Napoleons",
       "The Adventure Of The Three Students","The Adventure Of The Golden Pince-Nez",
       "The Adventure Of The Missing Three-Quarter","The Adventure Of The Abbey Grange",
       "The Adventure Of The Second Stain"]
ARB= [full_return[77:933],full_return[933:1970],full_return[1970:3052],full_return[3052:3874],
      full_return[3874:5293],full_return[5293:6207],full_return[6207:6911],full_return[6911:7789],
      full_return[7789:8616],full_return[8616:9582],full_return[9582:10534], full_return[10534:11497],
      full_return[11497:12656]]
Return_o_S = {}
for i in ART:
    Return_o_S[i] = ARB[ART.index(i)]

#Adventur_get = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
Adventure_get = open('the_adventures_of_sherlock_holmes.txt.utf-8')
full_adventure =  Adventure_get.readlines()
#Adventur stories titles
AST = ["A Scandal in A Scandal in Bohemia","Thr Red-Head Leauge",
       "A Case of Identitiy", "The Boscombe Valley Mystery","The Five Orange Pips",
       "The Man with the Twisted Lip","The Adventure of the Blue Carbuncle",
       "The Adventure of the Speckled Band","The Adventure of the Engineer's Thumb",
       "The Adventure of the Noble Bachelor","The Adventure of the Beryl Coronet",
       "The Adventure of the Copper Beeches"]
#Adventure Stories Books
ASB =[full_adventure[58:1188], full_adventure[1188:2297], full_adventure[2297:3100],
      full_adventure[3100:4229],full_adventure[4229:5124], full_adventure[5124:6230],
      full_adventure[6230:7209],full_adventure[7209:8417],full_adventure[8417:9384],
     full_adventure[9384:10410], full_adventure[10410:11539], full_adventure[11539:12682]]
Adventure = {}
for i in AST:
    Adventure[i] = ASB[AST.index(i)]


All_Titles = AST+ART+AMT+["A Study In Scarlet"]+["The Sign Of Four"]+["The Valley of Fear"]+["The Adventure of the Dying Detective"]+["The Adventure of The Cardboard Box"]+["The Adventure of the Wisteria Lodge"]+["The Last Bow"]+["The Hound of the Baskervilles"]
All_Stories = ASB+ARB+AMB+full_Study+full_Sugn+full_valley+full_Dying+full_Box+full_Lodge+full_bow+full_Hound
Titles_Stories = {"A Study In Scarlet":full_Study, "The Sign Of Four":full_Sugn, "The Valley of Fear":full_valley, "The Adventure of the Dying Detective":full_Dying, "The Adventure of The Cardboard Box":full_Box, "The Adventure of the Wisteria Lodge": full_Lodge, "The Last Bow": full_bow, "The Hound of the Baskervilles": full_Hound}
Titles_Stories.update(Adventure)
Titles_Stories.update(Return_o_S)
Titles_Stories.update(Memoirs)


#goal: sort this wiki page by headdings then look under the right headdings to find dates.
# I want to make a nested dictionary of sections so I can go check under cannon.
Bibliography = wikipedia.page("Canon of Sherlock Holmes")
Content = Bibliography.content.split('\n')
headings = {}
sub_headings = {}
sub_sub_headings = {}
Content_copy= Content
headdings_in_order = []
for i in Content_copy:
    if i[0:4] == '====':
        sub_sub_headings[i]= Content_copy.index(i)
        headdings_in_order.append(i)
        i = " "
    elif i[0:3] == '===':
        sub_headings[i]= Content_copy.index(i)
        headdings_in_order.append(i)
        i = " "
    elif i[0:2] == '==':
        headings[i]= Content_copy.index(i)
        headdings_in_order.append(i)
        i = " "
allheadingvals = {}
allheadingvals.update(sub_sub_headings)
allheadingvals.update(sub_headings)
allheadingvals.update(headings)
pieces = {}
for i in headdings_in_order:
    if headdings_in_order.index(i)+1 <  len(headdings_in_order):
        next_headding = headdings_in_order[headdings_in_order.index(i)+1]
        ip = allheadingvals[i]
        it = allheadingvals[next_headding]
        pieces[i]= Content[ip:it]
    else:
        pieces[i] = Content[allheadingvals[i]:]





def flatten(l):
    """
    This function flattens lists.
    """
    flatList = []
    for elem in l:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList


def remove_duplicate(values):
    """ This is a function that I added that removed duplicate strings from a
    list.
    """
    output = []
    seen = []
    for value in values:
        if value not in seen:
            output.append(value)
            seen.append(value)
    return (output)


def word_frequencies(story):
    """This function takes a set of lines and turns them into a dictionary
    with only unique words and word counts.

    I kinda got frusterated while writing this so is a little messed up...
    """
    flatten_story = flatten(story)
    single_string_story = ""
    fin = []
    words = []
    duhwords = []
    unique_words=[]
    dicty = {}
    for el in flatten_story:
        single_string_story = single_string_story + el
    words = single_string_story.split(" ")
    for i in words:
        mmm = i.split('\n')
        fin.append(mmm)
    fin2 = flatten(fin)
    for f in fin2:
        hope = ""
        for op in f:
            if str.isalpha(op) == False:
                g = ""
            elif str.islower(op) == False:
                g = str.lower(op)
            else:
                g = op
            hope +=g
        duhwords.append(hope)
    for pi in duhwords:
        if pi not in unique_words:
            unique_words.append(pi)
            dicty[pi] = 1
        else:
            dicty[pi] +=1
    return (unique_words, dicty)


def inverse_document_frequency(N, words):
    """
    This function takes a bunch of documents' unique_words
    N is number of texts. words is a list of unique words from all documents.
    the number of times a word is repeated in documents is the number of documents
    it is in.
    it N / 1+t
    """
    unique_words = []
    inv_dict = {}
    final_dict={}

    for el in words:
        if el not in unique_words:
            unique_words.append(el)
            inv_dict[el] = 1
        else:
            inv_dict[el] +=1
    for i in unique_words:
        final_dict[i] = math.log(N/(inv_dict[i]*1.00000000000))
    #print final_dict
    return final_dict


def final_vector(text_name):
    """This takes the word frequency dictionaries and spits out the vector of
    weighted frequency of each word.
    """
    frequencies = All_wordfewq_dict[text_name]
    final_frequency_list = []
    for el in all_unique_words:
        if el in frequencies:
            final_frequency_list.append(frequencies[el]*inverse_dict[el])
        else:
            final_frequency_list.append(0)
    return np.array(final_frequency_list)


def cosine_similarity(v1,v2,name):
    """
    this takes two lists and calculates their cosine similarity
    magsumv1 = 0
    magsumv2 = 0
    dotprod = 0
    for el in v1:
        magsumv1+=(el*1.0)**2
    for b in v2:
        magsumv2+= (b*1.0)**2
    magni = math.sqrt(magsumv1)*math.sqrt(magsumv2)
    for i in range(len(v1)):
        dotprod += v1[i] + v2[i]
    """

    return (np.dot(v1,v2)/((math.sqrt(sum(i**2 for i in v1)))*math.sqrt(sum(b**2 for b in v2))))
dates ={"A Scandal in A Scandal in Bohemia":(1891+(6.0/12)),"Thr Red-Head Leauge":((1891+(7.0/12))),
   "A Case of Identitiy":(1891+(8.0/12)), "The Boscombe Valley Mystery":(1891+(9.0/12)),"The Five Orange Pips":(1891+(10.0/12)),
   "The Man with the Twisted Lip":(1891+(11/12)),"The Adventure of the Blue Carbuncle":(1892),
   "The Adventure of the Speckled Band":(1892+(1/12)),"The Adventure of the Engineer's Thumb":(1892+(2/12)),
   "The Adventure of the Noble Bachelor":(1892+(3/12)),"The Adventure of the Beryl Coronet":(1892+(4/12)),
   "The Adventure of the Copper Beeches":(1892+(5/12)),"The Silver Blaze":(1892+(11/12)),"The Yellow Face":(1893+(1/12)),
   "The Stock-Broker's Clerk":(1893+(2/12)),"The Gloria Scott":(1893+(3/12)),
   "The Musgrave Ritual":(1893+(4/12)),"The Renigate Puzzle":(1893+(5/12)),
   "The Crooked Man":(1893+(6/12)),"The Resident Patient":(1893+(7/12)),
   "The Greek Interpreter":(1893+8/12),"The Naval Treaty":(1893+9/12),
   "The Final Problem":(1893+(11/12)), "The Adventure of The Cardboard Box":1893,"The Adventure Of The Empty House":(1903+(9/12)),
   "The Adventure Of The Norwood Builder":(1903+(10/12)), "The Adventure Of The Dancing Men":(1903+11/12),
   "The Adventure Of The Solitary Cyclist":(1904), "The Adventure Of The Priory School":(1904+(1/12)),
   "The Adventure Of Black Peter":(1904+(2/12)), "The Adventure Of Charles Augustus Milverton":(1904+(3/12)),
   "The Adventure Of The Six Napoleons":(1904+(4/12)), "The Adventure Of The Three Students":(1905+(5/12)),
   "The Adventure Of The Golden Pince-Nez":(1904+(6/12)), "The Adventure Of The Missing Three-Quarter":(1904+(7/12)),
   "The Adventure Of The Abbey Grange":(1904+(8/12)), "The Adventure Of The Second Stain":(1904+(9/12)),"The Hound of the Baskervilles":1902,
   "The Adventure of the Wisteria Lodge":1908, "The Adventure of the Dying Detective": 1913,
   "A Study In Scarlet":1887,"The Sign Of Four":1890,'The Last Bow': 1917,"The Valley of Fear":1915}

def whats_the_date(title):
    """ This function returns the date of a particlar sherlock holmes book.
    """
    return dates[title]


All_wordfewq_dict={}
all_words = []
all_unique_words = []


for el in Titles_Stories:
    boop = word_frequencies(Titles_Stories[el])
    All_wordfewq_dict[el] = boop[1]
    all_words.append(boop[0])

all_words = flatten(all_words)
all_unique_words = remove_duplicate(all_words)
inverse_dict = inverse_document_frequency(len(All_Titles),all_words)
Scarlet_vector = final_vector("A Study In Scarlet")
similarities = {}
years = {}

for el in All_Titles:
    years[el] = whats_the_date(el)
for key in All_wordfewq_dict:
    if key != "A Study In Scarlet":
        similarities[key] = cosine_similarity(Scarlet_vector,final_vector(key),key)
        plt.scatter(years[key],cosine_similarity(Scarlet_vector,final_vector(key),key))
for i in similarities:
    plt.annotate(i, (0, similarities[i]))
#print (final_vector("The Adventure Of The Abbey Grange"))
plt.show()
