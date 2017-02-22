import twitter
import os
import text_analyzer

# get auth from Twitter

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

user1 = input('User 1: ')
user2 = input('User 2: ')

# get statuses 1
statuses = api.GetUserTimeline(screen_name=user1, count=200)
file = open('data1.txt', 'w')
for items in statuses:
    file.write(items.text + "+++")

# get statuses 2
statuses = api.GetUserTimeline(screen_name=user2, count=200)
file = open('data2.txt', 'w')
for items in statuses:
    file.write(items.text + "+++")


text_analyzer.main(user1, user2)
