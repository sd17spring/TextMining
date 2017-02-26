"""
This file will retrieve the tweets of 4 French presidential candidates and return a graph of the 
sentiment analysis done on the candidates

Author: Emily Lepert
"""

import twitter
import numpy as np
import math
from unidecode import unidecode
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl

def retrieve_text(name, number):
	consumer_k = open('consumer_key.txt').read().strip()
	consumer_s = open('consumer_secret.txt').read().strip()
	access_key = open('access_token_key.txt').read().strip()
	access_secret = open('access_token_secret.txt').read().strip()
	api = twitter.Api(consumer_key=	consumer_k,
                  consumer_secret= consumer_s,
                  access_token_key= access_key,
                  access_token_secret= access_secret)

	l = open(name + '.txt', 'w')
	status = api.GetUserTimeline(screen_name='@' + name, count = number)

	for i in status:

		i = unidecode(i.text)
		l.write(i)
		l.write('\n')
		
	l.close()

def sentiment_analysis(name, dictionary):
	"""
	This function takes a file and creates a dictionary of each line's sentiment analysis.
	>>> sentiment_analysis('EmmanuelMacron', {})
	{'EmmanuelMacron': [0.1466666666666667, 0.0, -0.1, 0.0, 0.42000000000000004, 0.0, 0.115, 0.0, 0.1325, 0.0, 0.03333333333333333, 0.0, 0.27, -0.12, 0.0, 0.22, 0.27, 0.1, 0.15, 0.075, 0.0, 0.0, 0.0, 0.17, 0.0, 0.07666666666666666, 0.2, 0.0, 0.0, 0.2, 0.2525, -0.35, 0.0, 0.0, 0.1, 0.0, 0.15, 0.0, 0.0, 0.56, 0.0, 0.25, 0.22, 0.0, 0.0, 0.45, 0.0, 0.0, 0.023333333333333334, 0.025000000000000022, 0.0, 0.0, -0.125, 0.0, 0.0, 0.0, 0.15, 0.13666666666666666, 0.1, 0.11, 0.0, 0.0, -0.4, 0.0, 0.0, 0.2, 0.625, 0.0, 0.0, 0.0, 0.09999999999999999, 0.0, 0.05, 0.25, 0.0, 0.0, 0.0, 0.22, 0.0, 0.22, 0.22, 0.53, -0.15, 0.0, 0.0, 0.4, 0.0, 0.0, 0.009999999999999995, 0.0, 0.0, -0.016666666666666663, 0.1, 0.0, 0.15, 0.0, 0.1, 0.0, -0.25, 0.0, -0.25166666666666665, 0.22, 0.17, 0.0, 0.0, -0.7, 0.0, 0.22, 0.22, 0.0, 0.2, 0.0, 0.0, 0.0, 0.13, 0.17, 0.0, 0.1275, 0.0, 0.0, 0.1, 0.15, -0.16249999999999998, 0.1, 0.8, 0.14, 0.0, 0.0, -0.1, 0.0, 0.0, 0.0, 0.30833333333333335, 0.0, 0.185, 0.0, 0.0, 0.0, -0.09000000000000001, 0.0, 0.08, -0.75, 0.22, 0.0, -0.3, 0.21000000000000002, 0.010000000000000009, -0.03125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.17500000000000002, 0.3499999999999999, 0.09833333333333334, 0.135, 0.0, 0.0, 0.08, 0.2, 0.0, -0.2, 0.0, 0.2233333333333333, 0.0, 0.29, 0.0, 0.0, 0.0, 0.0, 0.6625000000000001, 0.29, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.32, 0.4, -0.24, 0.0, -0.125, 0.15, 0.0, 0.7, 0.0, 0.22, 0.0, 0.0, 0.5, 0.0, 0.2, -0.21875, 0.25, 0.26, 0.185, 0.08333333333333333, 0.23]}
	"""
	l = open(name + '.txt')
	lines = l.readlines()
	dictionary[name] = []
	for i in lines:
		blob = TextBlob(i, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
		dictionary[name].append(blob.sentiment[0])
	return(dictionary)

def create_dictionary(candidates):
	"""
	This creates a dictionary of the sentiment analysis for each candidate.
	The output is a dicitonary with the candidates' names as the key and the list
	of sentiment values as the value.
	"""
	dictionary = {}
	for i in candidates:
		dictionary = sentiment_analysis(i, dictionary)
	return(dictionary)
	

def graph(dictionary, candidates):
	"""
	Graphs the sentiment values for each candidate in different colors
	Hamon: red
	Macron: blue
	Fillon: green
	Lepene: yellow
	"""
	colors = ['blue', 'red', 'orange', 'green']
	# create an array of values that will be the x-axis of the graph
	# the list is consecutive numbers that go up to the numbers of tweets collected
	j = np.array(range(0, 202))
	# convert the numbers to the same type as the other numbers
	for i in candidates:
		dictionary[i] = np.array(dictionary[i])

	# plot the sentiments vs j list
	plt.plot(j, dictionary[candidates[0]], 'r-', j, dictionary[candidates[1]], 'b-', \
		j, dictionary[candidates[2]], 'g-', j, dictionary[candidates[3]], 'y-') 

	# legend specifications for each candidate and the corresponding color
	benoit_hamon = mpatches.Patch(color='red', label='Benoit Hamon')
	emmanuel_macron = mpatches.Patch(color='blue', label='Emmanuel Macron')
	francois_fillon = mpatches.Patch(color='green', label='Francois Fillon')
	marine_lepene = mpatches.Patch(color='yellow', label='Marine Lepene')

	# create legend
	plt.legend(handles=[benoit_hamon, emmanuel_macron, francois_fillon, marine_lepene])
	# axis labelling
	plt.xlabel('Tweet number')
	plt.ylabel('1 - Positive; -1 - Negative')
	# show the plot
	plt.show()


def ascending_dictionary(dictionary, candidates):
	"""
	Sorts the values of the dictionary in ascending order
	"""
	for i in candidates:
		dictionary[i] = sorted(dictionary[i])
	return(dictionary)

def threshold(dictionary, candidates):
	"""
	Finds the most negative and most positive sentiment values for each candidates
	"""
	maxes = []
	mins = []
	for i in dictionary:
		maxes.append(max(dictionary[i]))
		mins.append(min(dictionary[i]))

	print(maxes, mins)

def main():
	#list of candidates
	candidates = ['BenoitHamon', 'EmmanuelMacron', 'FrancoisFillon', 'MLP_officiel']
	# retrieves the tweets for the candidates
	#for i in range(4):
		#retrieve_text(candidates[i], 203)
	# create the dictionary sentiments
	sentiments = create_dictionary(candidates)
	#threshold(sentiments, candidates)

	#to see a sorted graph uncoment this line
	#sorted_sentiments = ascending_dictionary(sentiments, candidates)
	graph(sentiments, candidates)

if __name__ == '__main__':
    import doctest
    doctest.testmod()




