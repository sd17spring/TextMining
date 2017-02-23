import pickle
import requests

encyclopedia = requests.get('http://www.gutenberg.org/ebooks/41685.txt.utf-8')
f = open('britentries.pickle', 'wb')
pickle.dump(encyclopedia.text, f)
f.close()
