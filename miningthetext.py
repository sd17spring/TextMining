'''Gracey Wilson
Software Design Spring 2017
Mini Project 3: Text Mining

A script that grabs the text from ProjectGutenberg online and pickles it'''

import requests
romeo_juliet_full_text = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt').text
print(romeo_juliet_full_text)

import pickle

# Save data to a file (will be part of your data fetching script)
f = open('romeo_juliet_full_text.pickle', 'wb')
pickle.dump(romeo_juliet_full_text, f)
f.close()
