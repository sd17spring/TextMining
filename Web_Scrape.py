from twython import Twython
import pickle
import os

def read_key(name):
    f = open('secrets.txt')
    for line in f.readlines():
        if line.startswith(name):
            return line.split(':', 2)[-1].strip()

CONSUMER_KEY = read_key('CONSUMER_KEY')
CONSUMER_SECRET = read_key('CONSUMER_SECRET')
TOKEN_SECRET = read_key('ACCESS_TOKEN_SECRET')
TOKEN = read_key('TOKEN')

def create_file(filename, query):
    '''
    This function creates a new pickle file containing a list of tweets
    resulting from the input query.
    Inputs:
        filename - This is the name of the file you want to use to save the tweets in
        query - This is the twitter search query to use to search for tweets and can
                include operators like AND, OR and NOT, and also 'filter: retweets'
    '''


    # TOKEN = open('token.txt').read().strip()
    # TOKEN_SECRET = open('tokensecret.txt').read().strip()
    # CONSUMER_KEY = open('consumerkey.txt').read().strip()
    # CONSUMER_SECRET = open('consumersecret.txt').read().strip()

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)


    ##creating result as a dictionary from scraped data https://dev.twitter.com/rest/reference/get/search/tweets
    #we are using q because it signifies it's required and query, which is our input.
    result = t.search(q=query, count=1000, result_type = 'mixed')
    tweets = list()


    #appending list to inclue texts from statuses
    for status in result['statuses']:
        tweets.append(status['text'])
        print(status)


    # data['tweets'] = tweets
    # data['hashtags'] = tags

    filename += '.pickle'

    #user interaction when using pickle
    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(tweets,f)
        f.close()
        print('File created as %s.' % filename)
    else:
        response = input("File %s already exists. Replace existing? (Y/N):    " % filename)
        if response.lower() == 'y':
            f = open(filename,'wb')
            pickle.dump(tweets,f)
            f.close()
            print('File replaced as %s.' % filename)
        elif response.lower() == 'n':
            print('Action aborted.')


def open_file(filename):
    input_file = open(filename,'rb')
    tweets = pickle.load(input_file)
    input_file.close()
    return tweets


def main():
    create_file('trumptweets', "@realDonaldTrump -filter:retweets")
    create_file('obamatweets', "@BarackObama -filter:retweets")


if __name__ == '__main__':
    main()
