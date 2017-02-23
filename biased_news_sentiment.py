""" Analyzes the sentiment of articles from various biased news source.

    Written by Kyle Combes for Software Design (Spring 2017) Mini Project 3
    at Olin College of Engineering.
"""
from data_structures import *
from data_fetcher import DataFetcher
import matplotlib.pyplot as plt
from text_analyzer import TextAnalyzer


if __name__ == "__main__":

    # Define our sources. Format: {short_name:Source(short_name, display_name, rss_url, article_content_css_class)}
    sources = {'foxnews':Source('foxnews','FOX News','http://feeds.foxnews.com/foxnews/latest?format=xml','article-text'),
               'nytimes':Source('nytimes','NY Times','http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml','story-body'),
               'theguardian':Source('theguardian','The Guardian','https://www.theguardian.com/us/rss','content__article-body'),
               'infowars':Source('infowars','Infowars','http://www.infowars.com/feed/custom_feed_rss','text'),
               'breitbart':Source('breitbart','Breitbart','http://feeds.feedburner.com/breitbart?format=xml','entry-content'),
               'newyorker':Source('newyorker','The New Yorker','http://www.newyorker.com/feed/news','articleBody'),
               'dailykos':Source('dailykos','Daily Kos','http://www.dailykos.com/user/main/rss.xml','story-content'),
               'dailycaller':Source('dailycaller','Daily Caller','http://feeds.feedburner.com/dailycaller','article-content')}

    source_data = DataFetcher.fetch_latest_from_feeds(sources)
    x = []
    y = []
    labels = []

    # Analyze each source
    for source_name, data in source_data.items():
        scores = TextAnalyzer.get_ave_polarity_scores(data.articles)
        print('Analyzed %i articles from %s. Average scores:\n\t%s\n' % (scores['count'], source_name, scores))
        x.append(scores['pos'])
        y.append(scores['neg'])
        labels.append(data.name_full)

    # Plot the results
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Annotate the plot
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i]+0.0005,y[i]-0.0002), verticalalignment='center')

    plt.xlabel('Positivity')
    plt.ylabel('Negativity')
    plt.legend()
    plt.show()
