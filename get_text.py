import requests
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
book = requests.get('http://www.gutenberg.org/files/54214/54214-0.txt').text
book2 = requests.get('http://www.gutenberg.org/files/15616/15616-0.txt').text
book.lower()
book2.lower()
d = defaultdict(int)
for word in book.split():
    d[word] += 1
d2 = defaultdict(int)
for word in book2.split():
    d2[word] += 1
analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores(book))
print(analyzer.polarity_scores(book2))
