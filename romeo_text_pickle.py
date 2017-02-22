import pickle
import requests

romeo_text = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt').text
f = open('romeo.txt', 'wb')
pickle.dump(romeo_text, f)
f.close
