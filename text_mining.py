import requests
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

amontillado = requests.get('http://www.gutenberg.org/cache/epub/1063/pg1063.txt').text
raven = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt').text
house = requests.get('http://www.gutenberg.org/cache/epub/932/pg932.txt').text

def words(text):
    #This removed all of the non-alphanumeric characters in a given string
    return re.compile(r'\W+', re.UNICODE).split(text)

def makeDict(wlist):
    #This returns a dictionary of words and how frequently they appear in the story
    wfreq = [wlist.count(p) for p in wlist]
    return dict(zip(wlist,wfreq))

def sortDict(dfreq):
    #This sorts the dictionary created in makeDict
    sort = [(dfreq[key], key) for key in dfreq]
    sort.sort()
    sort.reverse()
    return sort

analyzer = SentimentIntensityAnalyzer()
analyzer2 = SentimentIntensityAnalyzer()
analyzer3 = SentimentIntensityAnalyzer()


if __name__ == "__main__":
    print(sortDict(makeDict(words(amontillado))))
    print(sortDict(makeDict(words(raven))))
    print(sortDict(makeDict(words(house))))
    print(analyzer.polarity_scores(amontillado))
    print(analyzer2.polarity_scores(raven))
    print(analyzer3.polarity_scores(house))
