import praw
from praw.models import MoreComments
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

defaults = 'announcements+Art+AskReddit+askscience+aww+blog+books+creepy+dataisbeautiful'

def read_key(name):
    return open(name + '.txt').read().strip()

def data_pull(subreddit_names):
    CLIENT_ID = read_key('Reddit_clientID')
    CLIENT_SECRET = read_key('Reddit_Secret')
    r = praw.Reddit(user_agent='linux:text_mining:v0.0.0 (by /u/sd17springtanthony)',
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET)
    for name in subreddit_names:
        submissions = r.subreddit(name).hot(limit=5)
        # print([x.title for x in submissions]
        comments = []
        comment_score = []
        f = open(name + '.pickle', 'wb')
        for post in submissions:
            post.comments.replace_more(limit=0)
            # comments = [post.score + "\n \n \n"]
            for comment in post.comments.list():
                comments.append(comment.body)
                comment_score.append(comment.score)
                # print(comments)
        pickle.dump(comments,f)
        pickle.dump(comment_score,f)
        f.close()

def data_load(subreddit_names):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = {} # key:  Comment.  Entry: average sentiment
    sentiments = [] # Average sentiment of each subreddit
    for sub in subreddit_names:
        input_file = open(sub + '.pickle', 'rb')
        reloaded_data = pickle.load(input_file) #Reload comment list
        # print(reloaded_data)
        reloaded_scores = pickle.load(input_file) # Reload scores of comments
        # print(reloaded_scores)
        #Create score dictionary
        score_dict = zip(reloaded_data,reloaded_scores) 
        comment_sent_dict = {}
        comment_sentiments = [] #initialize comment sentiment array
        for comment in reloaded_data:
            analyzer.polarity_scores(comment)
            #Add element to dictionary of sentiment by comment
            comment_sent_dict[comment] = analyzer.polarity_scores(comment)['compound']
            # Add element to sentiment array
            comment_sentiments.append(comment_sent_dict[comment])
            # comment_sent_dict = sentiment_dict[comment]
            # print(sentiment_dict[comment])
        #Find average sentiment for the subreddit
        ave_sentiment = sum(comment_sentiments)/len(comment_sentiments)
        sentiments.append(ave_sentiment)
        sentiment_dict[sub] = ave_sentiment
    print("sentiment dictionary is:",sentiment_dict)
def main():
    subreddits = ["all","popular","politics"]
    # data_pull(subreddits)
    data_load(subreddits)

if __name__ == '__main__':
    main()