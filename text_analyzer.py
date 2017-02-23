""" Performs sentiment analysis on a scraped article using VaderSentiment

    Written by Kyle Combes for Software Design (Spring 2017) Mini Project 3
    at Olin College of Engineering.
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
class TextAnalyzer:

    def get_ave_polarity_scores(articles):
        analyzer = SentimentIntensityAnalyzer()
        pos = 0
        neu = 0
        neg = 0
        compound = 0
        empty_article_count = 0
        for url,article in articles.items():
            if article.content == None or len(article.content) < 100:
                # Don't count empty articles or articles less than 100 characters (probably not a valid article)
                empty_article_count += 1
                continue
            scores = analyzer.polarity_scores(article.content)
            pos += scores['pos']
            neu += scores['neu']
            neg += scores['neg']
            compound += scores['compound']
        #print('No content for %i articles. Not including in analysis.' % empty_article_count)
        count = len(articles.items()) - empty_article_count
        pos = pos / count
        neu = neu / count
        neg = neg / count
        compound = compound / count
        return {'pos':pos, 'neu':neu, 'neg':neg, 'compound':compound, 'count':count}
