import requests
import pickle
import wikipedia
#print(requests.get('http://google.com').text)

#oliver_twist_full_text = requests.get('http://www.gutenberg.org/ebooks/730.txt.utf-8').text
#print(oliver_twist_full_text)
"""olin = wikipedia.page("Olin College")


# Save data to a file (will be part of your data fetching script)
#f = open('files//dickens_texts.txt','wb')
#pickle.dump(oliver_twist_full_text, f)
#f.close()
f = open('files//olin.pickle','wb')
pickle.dump(olin.content, f)
f.close()

# Load data from a file (will be part of your data processing script)
input_file = open('files//olin.pickle','rb')
reloaded_copy_of_texts = pickle.load(input_file)
print(reloaded_copy_of_texts)"""

testlist = [1, 2, 3, 4, 5, 3, 2]
index = testlist.index(3)
print(index)
