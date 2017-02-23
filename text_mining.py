"""
text_mining.py
Tatiana Anthony
* Pulls 100 comments from /r/all, /r/popular (for defaults), the 15 largest 
subreddits as of Thursday Febrary 23, 2017 at 9:30 AM, and a few subreddits I
was interested in.
* Pickles them to save the comments and scores of the comments.
* Runs sentiment analysis on the comments
* Scales sentiment by the score of the comment
    - A positive comment that is upvoted will increase the subreddit sentiment
    - A negative comment that is upvoted will decrease the subreddit sentiment
    - A positive comment that is downvoted will decrease the subreddit sentiment
    - A negative comment that is downvoted will increase the subreddit sentiment
* Graphs the sentiments of each subreddit.
"""
import praw
from praw.models import MoreComments
from os.path import exists
import pickle
import numpy as np
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

defaults = 'announcements+Art+AskReddit+askscience+aww+blog+books+creepy+dataisbeautiful'

def read_key(name):
    """
    Inputs:  name of the read key file
    Outputs:  The key
    """
    return open(name + '.txt').read().strip()

def data_pull(subreddit_names,numposts):
    """
    Inputs:  list of subreddit names, number of posts to look at
    Outputs: None.
    Files created:  Pickle file for each subreddit, with comments and scores
    """
    # Setup PRAW
    CLIENT_ID = read_key('Reddit_clientID')
    CLIENT_SECRET = read_key('Reddit_Secret')
    r = praw.Reddit(user_agent='linux:text_mining:v0.0.0 (by /u/sd17springtanthony)',
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET)

    # Pull the comments and scores
    for name in subreddit_names: #Loop through subreddits
        submissions = r.subreddit(name).hot(limit=numposts) #Get submissions
        comments = [] #Instantiate comment list
        comment_score = [] # instantiate score list
        f = open(name + '.pickle', 'wb') #Open a pickle file for subreddit
        postnum = 1 #Keep track of how many posts have gone
        for post in submissions: #Loop through posts
            post.comments.replace_more(limit=0) #Get comments
            for comment in post.comments.list(): #Loop through comments
                comments.append(comment.body) #Add commment to list
                comment_score.append(comment.score) # Add score to list 
            #Tell user how many posts have gone
            print("finished post number", postnum, " in ", name)
            postnum += 1 #keep track

        pickle.dump(comments,f) #Save the comments
        pickle.dump(comment_score,f) #save the scores
        f.close() #close the pickle file

def data_load(sub):
    """
    inputs:  Subreddit name
    Outputs:  comment list, score list
    Loads the comments and scores from a subreddit pickle file
    """
    input_file = open(sub + '.pickle', 'rb')
    reloaded_data = pickle.load(input_file) #Reload comment list
    reloaded_scores = pickle.load(input_file) # Reload scores of comments
    input_file.close()
    return reloaded_data, reloaded_scores

def sentiment_load():
    """ 
    Input: None
    Outputs:  subreddit list, mean sentiment list, standard deviation list.
    Loads the subreddits, sentimetns, and standard deviatoins from pickle for graphing
    """
    input_file = open('Sentiment.pickle', 'rb')
    subreddits = pickle.load(input_file) #Reload subreddits
    means = pickle.load(input_file) # Reload averages
    stds = pickle.load(input_file) # Reload standard deviations
    input_file.close()
    return subreddits,means,stds

def data_sent_analyze(subreddit_names,numposts):
    """
    Inputs:  Subreddit names, number of posts.
    Outputs:  Sentiment list, standard deviation list, dictionary of subreddits and sentiments
    Saves:  Pickle file of subreddits, sentiments, average sentiments, standard deviations
    Analyzes the sentiment of comments from each subreddit in a list.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = {} # key:  Comment.  Entry: average sentiment
    sentiments_mean = [] # Average sentiment of each subreddit
    sentiments_std = [] # Average Deviation of each subreddit
    for sub in subreddit_names:
        if exists(sub+".pickle") == False:
            data_pull(sub,numposts)
        reloaded_data, reloaded_scores = data_load(sub) #Load data from pickle
        comment_sentiments = [] #initialize comment sentiment array
        for i in range(len(reloaded_data)):
            #Add element to dictionary of sentiment by comment
            comment_sent = analyzer.polarity_scores(reloaded_data[i])['compound']*reloaded_scores[i]
            # Add element to sentiment array
            comment_sentiments.append(comment_sent)
        #Find average and std of sentiment for the subreddit
        ave_sentiment = np.mean(comment_sentiments)
        std_sentiment = np.std(comment_sentiments)
        sentiments_mean.append(ave_sentiment)
        sentiments_std.append(std_sentiment)
        sentiment_dict[sub] = ave_sentiment #Put in sentiment dictionary
        print('Sentiment analysis done for /r/', sub) #give user feedback
    #Save the arrays
    f = open('Sentiment.pickle', 'wb')
    pickle.dump(subreddit_names,f)
    pickle.dump(sentiments_mean,f)
    pickle.dump(sentiments_std,f)
    f.close()
    #Print out sentiment dictionary
    print("sentiment dictionary is:",sentiment_dict)
    return sentiments_mean,sentiments_std,sentiment_dict

def graph_stuff(subreddits,mean,std):
    """
    Inputs:  subreddit, mean sentiments, standard deviation
    Outputs:  Graph
    Saves: Graph
    Graphes the subreddit sentiments"""
    ind = np.arange(len(subreddits))  # the x locations for the groups
    width = 0.75       # the width of the bars

    fig, ax = plt.subplots() #Initiate figure
    colors = []
    #Makes positive blue and negative red
    for i in range(len(subreddits)):
        # print(i)
        if mean[i] > 0:
            colors.append('b')
        else:
            colors.append('r')
    rects1 = ax.bar(ind, mean, width, color=colors) # Makes bar chart
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Sentiment of Subreddit')
    ax.set_title('Sentiment of Each Subreddit')
    ttl = ax.title
    ttl.set_position([.5, 1.05]) #change title position
    ax.set_xticks(ind)
    ax.set_xticklabels(subreddits, rotation=60, ha = 'right')
    fig.tight_layout() #Makes it so labels all show


    def autolabel(rects,values):
        """
        Helper function:
        Attach a text label to each bar near the axis
        """
        for i in range(len(rects)):
            rect = rects[i]
            val = mean[i]
            if mean[i] > 0:
                location = -1.75
                height = rect.get_height()
            else:
                location = .5
                height = -rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,  location,
                    '%.2f' % height,
                    ha='center', va='bottom',rotation=90)

    autolabel(rects1,mean)
    plt.show() #shot the plot
    plt.savefig("Subreddit Sentiment Analysis") #save the plot

def main():
    """
    Pull text from reddit, analyze, and plot it.
    """
    numposts=100
    subreddits = [
                  "all","popular", #defaults
                  "AskReddit","funny","todayilearned","science","worldnews",
                  "pics","IAmA","announcements","gaming","videos",
                  "movies","blog","Music","aww","news", #end of top 15
                  "politics","happy","TwoXChromosomes","TheRedPill","relationships",
                  "personalfinance","tifu"]
    data_pull(subreddits,numposts) #Pulls data_pull
    #Calculates Sentiments 
    sentiments_mean,sentiments_std,sentiment_dict = data_sent_analyze(subreddits,numposts)
    # subreddits, sentiments_mean,sentiments_std = sentiment_load() #Loads sentiments
    graph_stuff(subreddits, sentiments_mean, sentiments_std) #Plot sentiment 

if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit(main, number=1))
    main()