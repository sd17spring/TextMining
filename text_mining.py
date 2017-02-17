import requests
import pickle
import wikipedia

communist_manifesto = requests.get('http://www.gutenberg.org/files/23905/23905-readme.txt').text
#print(oliver_twist_full_text)

f = open('communist_manifesto.pickle','wb')
pickle.dump(communist_manifesto,f)
f.close()

# Load data from a file (will be part of your data processing script)
input_file = open('communist_manifesto.pickle','rb')
reloaded_copy_of_texts = pickle.load(input_file)
