import requests
import pickle
website = 'http://cnn.com'
sampleText = requests.get(website).text
f = open('cnn.pickle', 'wb')
pickle.dump(sampleText, f)
f.close()
