"""
NAME: Prava

Data source: Wikipedia (specifically the page for Olin)
For first deliverable and data mining, this program prints the top words and
creates a word cloud for the Olin wikipedia page.

"""

from text_analysis import count_words, top50_cloud
import wikipedia

# gets the data from Olin
olin = wikipedia.page("Olin College")

# removes the stuff at the end using the last word
olin_wiki = olin.content[0:olin.content.index('lows.') + len('lows.')]

# stop words
f = open('/home/prava/TextMining/stopwords.txt')
# read the file and get stop words
stop_words = f.read().split()
f.close()

words = count_words(olin_wiki, stop_words)
top50_cloud(words, 'Top words for Olin Wikipedia page', 'WORD\tCOUNT')
