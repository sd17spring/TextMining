import pickle
import requests

# get koran text form project gutenberg
koran = requests.get(
    'http://www.gutenberg.org/cache/epub/2800/pg2800.txt').text

'''
create and open new writable file to dump koran text into
this pickle file is used to create koran.txt by copying and pasting
an excerpt manually
'''
f = open('koran.pickle', 'wb')
pickle.dump(koran, f)
f.close()
