"""
Uses the Twitter API to gather 200 tweets from two people,
analyzes the tweets for sentiment, and displays the results.

@Author: Peter Seger 2017
"""

from os import path
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Open the data1.txt file and read each tweet broken up by '+++'
with open('data1.txt', 'r') as f:
    temp = f.read()
tweets1 = temp.split('+++')

# Open the data2.txt file and read each tweet broken up by '+++'
with open('data2.txt', 'r') as f:
    temp = f.read()
tweets2 = temp.split('+++')


def build_data(tweets):
    """
    Builds a dictionary of all the words in all the tweets for frequency
    """
    d = dict()
    throwaway_terms = dict()
    master_list = []
    for tweet in tweets:
        master_list.append(tweet.split())
    for tweets in master_list:
        for words in tweets:
            if words[0] == 'h' and words[1] == 't' and words[2] == 't':
                throwaway_terms[words] = d.get(words, 0) + 1
            else:
                d[words] = d.get(words, 0) + 1
    return d


def total_word(data):
    """
    Calculates the total number of differnet values in the tweet dictionary
    """
    return sum(data.values())


def most_common(person, data):
    """
    Takes a dictionary of all the words in the tweets
    Prints the top 10 most common words
    """
    res = []
    for key, value in data.items():
        res.append((value, key))

    res.sort(reverse=True)
    print("The most common words for %s are: " % (person))
    for freq, word in res[:10]:
        print(word, freq, sep='\t')


def most_common_data(person, data):
    """
    Takes a dictionary of all the words in the tweets
    Prints the top 10 most common words
    """
    res = []
    for key, value in data.items():
        res.append((value, key))
    return res


def sentiment_analysis(tweets):
    """
    Reads a list of all the tweets and uses sentiment analysis
    Returns a list of the 'compound' sentiment for each tweet
    """
    analyzer = SentimentIntensityAnalyzer()
    a = []
    for i in tweets:
        temp1 = analyzer.polarity_scores(i)
        a.append(temp1.get('compound'))
    return a


def compound_sentiment_analysis(scores):
    """
    Takes a set of sentiment analysis scores
    Returns the average sentiment of all the tweets
    """
    total = 0.0
    j = 0
    while j < len(scores) - 1:
        total = total + scores[j]
        j += 1
    return total / len(scores)


def word_map():
    """
    Uses the word_coud library from amueller to create a word cloud of words
    https://github.com/amueller/word_cloud
    """
    d = path.dirname(__file__)
    text = open(path.join(d, 'data.txt')).read()
    wordcloud = WordCloud(max_font_size=600).generate(text)
    image = wordcloud.to_image()
    image.save('test.png')
    image.show()


def plot_word_frequency(d):
    """
    Built with the help of Randal Olson
    http://bit.ly/1uBkJI5
    """
    plt.figure(figsize=(12, 9))

    # remove frame lines
    ax = plt.subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Adjust tick mark size
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=14)
    plt.yticks(range(0, 200, 20), fontsize=14)

    # set axis labels
    plt.xlabel('Words', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)

    # plot it
    plt.hist(d, bins=10)

    # save it!
    plt.savefig('WordFreqency1.jpg', bbox_inches='tight')


def plot_sentiment(user1, user2, a, b):
    """
    Plots a scale of sentiment
    code used from searborn
    https://seaborn.pydata.org/examples/color_palettes.html
    """
    data1 = a
    data2 = b

    sns.set(style='white', context='talk')
    rs = np.random.RandomState(1)

    # setup the matplotlib figure
    f, (ax1) = plt.subplots(1, 1, figsize=(8, 6), sharex=True)

    # Put data in
    x = np.array([user1, user2])
    y1 = np.array([a, b])
    sns.barplot(x, y1, palette='BuGn_d', ax=ax1)
    ax1.set_ylabel('Sentiment')

    # finalize plot
    sns.despine(bottom=True)
    plt.setp(f.axes, yticks=[])
    plt.tight_layout(h_pad=3)
    plt.savefig(filename='Tester_6.jpg')


def main(user1, user2):
    """
    Does all the compiling
    Returns: most common words for user1
            most common words for user 2
            sentiment analysis for user1
            sentiment analysis for user2
    """
    processed_tweets1 = build_data(tweets1)
    processed_tweets2 = build_data(tweets2)

    data1 = most_common_data(user1, processed_tweets1)
    data2 = most_common_data(user2, processed_tweets2)

    most_common(user1, processed_tweets1)
    most_common(user2, processed_tweets2)

    a = sentiment_analysis(tweets1)
    b = sentiment_analysis(tweets2)

    print(user1 + ': ' + str(compound_sentiment_analysis(a)))
    print(user2 + ': ' + str(compound_sentiment_analysis(b)))

    # plot_word_frequency(data1)
    a2 = compound_sentiment_analysis(a)
    b2 = compound_sentiment_analysis(b)
    plot_sentiment(user1, user2, a2, b2)


if __name__ == "__main__":
    main('Trump', 'Obama')
