import wikipedia
import nltk
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pickle
page1=wikipedia.page('Olin College')
list1=nltk.word_tokenize(page1.content)
page2=wikipedia.page('Stanford University')
list2=nltk.word_tokenize(page2.content)
concatlist1=[]
concatlist2[]
from collections import Counter

def no_repeat(list1, list2):
    for i in list1:
        if i not in concatlist1:
            concatlist1.append(i)
    for i in list2:
        if i not in concatlist2:
            concatlist2.append(i)
    return concatlist1, concatlist2


compiled=[]
def similarity(concatlist1, concatlist2):
    i=0
    for i in list1[i]:
        if list1[i] in list2:
            compiled.append[list1]
        else:
            i+=1
    return compiled

analyzer = SentimentIntensityAnalyzer()
analyzer.polarity_scores(concatlist1)
analyzer.polarity_scores(concatlist2)

def pickle(list1, list2):
    f1 = open('list1.pickle','wb')
    pickle.dump(list1,f)
    f1.close()
    f2 = open('list2.pickle','wb')
    pickle.dump(list2,f)
    f2.close()
    return f1, f2


def process_file(f1,f2):
    hist= dict()
    fp1=open(f1)
    for item in fp1:
        hist[item]=hist.get(word,0)+1
    return hist

    # counts1=Counter(list1)
    # counts2=Counter(list2)
    # return counts1
    # return counts2

def counter(concatlist1, concatlist2):
    for i in concatlist1:
        concatlist1.count(i)
