# data source: project gutenberg
# printing sherlock holmes full text and make them as one list of texts

import pickle
import requests


adventure_of_sherlock_holmes = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
print(adventure_of_sherlock_holmes)


# Save data to a file
f = open('adventure_of_sherlock_holmes.pickle', 'wb')
pickle.dump(adventure_of_sherlock_holmes, f)
f.close()

# Load data from a file
input_file = open('adventure_of_sherlock_holmes.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)
