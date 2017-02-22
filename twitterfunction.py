import twitter
import pickle
def pull_tweets(id_max):
    CONSUMER_KEY = '*'
    CONSUMER_SECRET = '*'
    ACCESS_TOKEN_KEY = 	'*'
    ACCESS_TOKEN_SECRET = '*'

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)
    tweets = api.GetUserTimeline(screen_name='realDonaldTrump', count = 199, max_id = id_max)
    for status in tweets:
        print(status.id)
        print(status.created_at)

    #converts the information pulled into a string.
    tweets_string = str(tweets)
    return tweets_string

def access_twitter ():
    '''
    This function pulls a bunch of tweets from a user, and stores them in a file which is accessed by another program later.
    '''
    #The maximum tweets that can be pulled at one time is 200, so I manually ran
    #through pulling 200 at a time grabbing the last tweet key for each
    #I put them in the array below, so this is now a one step process
    max_id = [821772494864580614, 808837073423794176, 795311315304714242,
    789573953144680448, 786285509668696065, 782313153308884992,
    775293160838819841, 767505383430782976, 759506712516784128,
    754747397700485120, 746908869134262272, 739576535561162752, 732736781351849989, 726918444931776512, 719001329759363072, 712357352972939265, 710453513155960834]
    #Keys used to access twitter


    #call function to pull the tweets
    all_tweets = ""
    for max_ids in max_id:
        current_tweets = pull_tweets(max_ids)
        #print(current_tweets)
        print()
        print()
        all_tweets = all_tweets + (current_tweets)
    #print (tweets_string)
    #uses pickle to store the information in a file

    files = open("trump_tweets2.txt", 'wb')
    pickle.dump(all_tweets, files)
    files.close


    #puts it in a readable file, so I can read it
    files = open("trump_tweet_readable2.txt", 'w')
    files.write(all_tweets)
    files.close

if __name__ == "__main__":
    access_twitter()
