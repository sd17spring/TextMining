"""
MP3: Chef Gordon Ramsay's Sentiment Analysis on Twitter
@ilya-besancon
February 2017
"""
import twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main():
    """ Gets last 200 tweets from Chef's Twitter Page """
    CONSUMER_KEY = '3sqEK5AwQUI32isQAV4LGTdDa'
    CONSUMER_SECRET = '9xjKjy5oovPD5fBeH3JwI4gBjPVwSmaqFUAXW0eLEE7A0yvTwZ'
    ACCESS_TOKEN_KEY = '833009544758444033-K7Kb08YAz5uMHXc2jFzCDeiCq5SJhyQ'
    ACCESS_TOKEN_SECRET = 'gPqGBcsY0YDCVY3wcfVIj2DhgV6y3JtRVMRxDQjpr8yNE'

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    tweets = api.GetUserTimeline(screen_name='GordonRamsay', count=200)
    return tweets


def parse_list_tweets():
    """ Returns list of text from tweets """
    # gets tweets from main():
    tweetlist = main()
    # parses text from each tweet into list:
    tweet_text = [s.text for s in tweetlist]
    return tweet_text


def sentiment_analysis():
    """ Returns: {'compound': 0.5093, 'neg': 0.0, 'neu': 0.603, 'pos': 0.397} """
    # gets list of text of each tweet:
    tweet_text = parse_list_tweets()
    # total will be used to take average compound sentiment
    total = 0
    analyzer = SentimentIntensityAnalyzer()
    for sentence in tweet_text:
        score = analyzer.polarity_scores(sentence)
        # tallies compound score of each tweets
        total += score['compound']
    # divides total by number of tweets
    average = str(total/len(tweet_text))
    # returns the value to 3 decimal places
    return average[:5]


if __name__ == '__main__':
    avg = sentiment_analysis()
    print("Average Sentiment of 200 Chef Gordon Ramsay's Tweets: ", avg)
