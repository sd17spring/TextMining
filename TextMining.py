'''''
Software Design Project 3: Text Mining
@author Margaret Rosner

'''''

import random
import math
from random import randint
import requests

herland_full_text = requests.get('http://www.gutenberg.org/files/32/32-0.txt').text
crusoe_full_text = requests.get('http://www.gutenberg.org/files/521/521-0.txt').text

#first remove all punctuation from the texts
import string
s1 = herland_full_text # do you just put the whole text here?
#out1 = s1.translate(string.punctuation)
s2 = crusoe_full_text # Sample string
#out2 = s2.translate(string.punctuation)
exclude = set(string.punctuation)
s1 = ''.join(ch for ch in s1 if ch not in exclude)
s2 = ''.join(ch for ch in s2 if ch not in exclude)

#make all letters lowercase
herland_text = str.lower(s1)
crusoe_text = str.lower(s2)

whole_text = herland_text + crusoe_text

#print(whole_text)

word_list = whole_text.split(' ')

#make an index of all words in Herland & Crusoe
new_dict = {}
""" The following code creates a dictionary (new_dict) that contains all of the
words in both texts as keys and then the word that
follows the key word stored in a dictionary. If the word already exists in the
dictionary the code simply adds the following word in the list to the dictionary.
"""
for index,word in enumerate(word_list[:-1]):
    if word not in new_dict:
        new_dict[word] = [word_list[index + 1]]
    else:
        new_dict[word].append(word_list[index + 1])
#print(new_dict)

def quote(data,length_quote):
    """ This function generated a random sentence/quote from the dictionary
    created above. this code randomly chooses an index and then finds the key
    with that index in the dictionary and then randomly chooses a value of that
    key. That value is then added to a string and then becomes the next key.
    This process is repeted until the desired length of quote is reached.
    """
    new_string = '"'
    num_words = 0
    x = random.choice(list(data.keys()))
    while num_words < length_quote:
        if num_words > 0:
            new_string += ' '
            #print(new_string)
        next_word = random.choice(data[x])
        new_string = new_string + next_word
        x = next_word
        num_words = num_words + 1
    new_string += '."'
    #print(new_string)
    return new_string



Herland_Crusoe = quote(new_dict, 30)
print(Herland_Crusoe)
