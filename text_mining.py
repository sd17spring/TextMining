import praw
from praw.models import MoreComments
from os.path import exists
import pickle
import numpy as np
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

defaults = 'announcements+Art+AskReddit+askscience+aww+blog+books+creepy+dataisbeautiful'

def read_key(name):
    return open(name + '.txt').read().strip()

def data_pull(subreddit_names,numposts):
    CLIENT_ID = read_key('Reddit_clientID')
    CLIENT_SECRET = read_key('Reddit_Secret')
    r = praw.Reddit(user_agent='linux:text_mining:v0.0.0 (by /u/sd17springtanthony)',
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET)
    for name in subreddit_names:
        submissions = r.subreddit(name).hot(limit=numposts)
        # print([x.title for x in submissions]
        comments = []
        comment_score = []
        f = open(name + '.pickle', 'wb')
        postnum = 1
        for post in submissions:
            post.comments.replace_more(limit=0)
            # comments = [post.score + "\n \n \n"]
            for comment in post.comments.list():
                comments.append(comment.body)
                comment_score.append(comment.score)
                # print(comments)
            print("finished post number", postnum, " in ", name)
            postnum += 1
        pickle.dump(comments,f)
        pickle.dump(comment_score,f)
        f.close()

def data_load(sub):
    input_file = open(sub + '.pickle', 'rb')
    reloaded_data = pickle.load(input_file) #Reload comment list
    # print(reloaded_data)
    reloaded_scores = pickle.load(input_file) # Reload scores of comments
    # print(reloaded_scores)
    input_file.close()
    return reloaded_data, reloaded_scores

def sentiment_load():
    input_file = open('Sentiment.pickle', 'rb')
    subreddits = pickle.load(input_file) #Reload subreddits
    # print(reloaded_data)
    means = pickle.load(input_file) # Reload averages
    # print(reloaded_scores)
    stds = pickle.load(input_file) # Reload standard deviations
    input_file.close()
    return subreddits,means,stds

def data_sent_analyze(subreddit_names,numposts):
    
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = {} # key:  Comment.  Entry: average sentiment
    sentiments_mean = [] # Average sentiment of each subreddit
    sentiments_std = [] # Average Deviation of each subreddit
    for sub in subreddit_names:
        if exists(sub+".pickle") == False:
            data_pull(sub,numposts)
        reloaded_data, reloaded_scores = data_load(sub)
        #Create score dictionary
        # score_dict = dict(zip(reloaded_data,reloaded_scores))
        # comment_sent_dict = {}
        comment_sentiments = [] #initialize comment sentiment array
        # for comment in reloaded_data:
        #     #Add element to dictionary of sentiment by comment
        #     comment_sent = analyzer.polarity_scores(comment)['compound']
        for i in range(len(reloaded_data)):
            #Add element to dictionary of sentiment by comment
            comment_sent = analyzer.polarity_scores(reloaded_data[i])['compound']*reloaded_scores[i]
            # comment_sent_dict[comment] = comment_sent
            # Add element to sentiment array
            comment_sentiments.append(comment_sent)
            # comment_sent_dict = sentiment_dict[comment]
            # print(sentiment_dict[comment])
        #Find average sentiment for the subreddit
        ave_sentiment = np.mean(comment_sentiments)
        std_sentiment = np.std(comment_sentiments)
        sentiments_mean.append(ave_sentiment)
        sentiments_std.append(std_sentiment)
        sentiment_dict[sub] = ave_sentiment
        print('Sentiment analysis done for /r/', sub)
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
    ind = np.arange(len(subreddits))  # the x locations for the groups
    width = 0.75       # the width of the bars

    fig, ax = plt.subplots()
    colors = []
    for i in range(len(subreddits)):
        # print(i)
        if mean[i] > 0:
            colors.append('b')
        else:
            colors.append('r')
    # rects1 = ax.bar(ind, mean, width, color=colors, yerr=std)
    rects1 = ax.bar(ind, mean, width, color=colors)
    
    # rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Sentiment of Subreddit')
    ax.set_title('Sentiment of Each Subreddit')
    ttl = ax.title
    ttl.set_position([.5, 1.05])
    # fig.top(1.05)
    ax.set_xticks(ind)
    ax.set_xticklabels(subreddits, rotation=60, ha = 'right')
    # ax.tick_params(pad=20)
    fig.tight_layout()

    # ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


    def autolabel(rects,values):
        """
        Attach a text label above each bar displaying its height
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
    # autolabel(rects2)

    plt.show()
    plt.savefig("Subreddit Sentiment Analysis")
    

def main():
    numposts=100
    subreddits = [
                  "all","popular", #defaults
                  "AskReddit","funny","todayilearned","science","worldnews",
                  "pics","IAmA","announcements","gaming","videos",
                  "movies","blog","Music","aww","news", #end of top 15
                  "politics","happy","TwoXChromosomes","TheRedPill","relationships",
                  "personalfinance","tifu"]
    # data_pull(subreddits,numposts)
    # sentiments_mean,sentiments_std,sentiment_dict = data_sent_analyze(subreddits,numposts)
    subreddits, sentiments_mean,sentiments_std = sentiment_load()
    graph_stuff(subreddits, sentiments_mean, sentiments_std)

if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit(main, number=1))
    main()