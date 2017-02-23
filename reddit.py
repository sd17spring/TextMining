import praw
import requests
import requests.auth
import pprint
"""
This file takes comments from /r/totallynotrobots and generates a text file which can be the processed by another python program
"""

#PRAW setup
infoFile = open("redditInfo.txt")
secretInfo = infoFile.readlines()
reddit = praw.Reddit(user_agent='text_mining', client_id=secretInfo[0].strip(), client_secret=secretInfo[1].strip(),username=secretInfo[2].strip(),password=secretInfo[3].strip())
sub = reddit.subreddit('totallynotrobots')



def getCommentsAsText(sub,posts):
    textFile = open("data.txt",'w')
    for x in range(posts):
        submission = (next(x for x in sub.top() if not x.stickied))
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            textFile.write(comment.body.strip())
            textFile.write("\n")
    textFile.close()

def getFrequency(sub):
    frequency = {}
    for x in range(5):
        submission = (next(x for x in sub.top() if not x.stickied))
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            for words in comment.body.split():
                frequency[words] = frequency.get(words,0)+1

    sortedFrequency = sorted(frequency, key=frequency.__getitem__, reverse = True)

    textFile = open("frequencies.txt",'w')        
    for key in sortedFrequency:
        textFile.write("%r: %r" %(key,frequency[key]))
        textFile.write("\n")
    textFile.close()
getCommentsAsText(sub,30)
exec(open("markovRobots.py").read())
