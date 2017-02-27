from Tokenization import *
import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def create_text(hist):
    '''
    converts dictionary to string based on word frequencies.
    Keys = String words
    Value = Int word frequencies
    '''
    result = str()
    for i in hist:
        for j in range(hist[i]):
            result = result + ' ' + i
    return result

def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def sentiments(text):
    '''
    This compiles a list of sentiment results of each tweet in text.
    text: list of tweets
    '''
    result = []
    for tweet in text:
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        result.append(score)

    return result

def positivity(x):
    pos = float()
    for i in x:
        pos += i['pos']
    pos = pos/len(x)
    return pos

def negativity(x):
    neg = float()
    for i in x:
        neg += i['neg']
    neg = neg/len(x)
    return neg

def main():
    trump = open_file('trumptweets.pickle')
    obama = open_file('obamatweets.pickle')

    trumps = sentiments(trump)
    obamas = sentiments(obama)

    write_file(trumps, 'sentiments_trump')
    write_file(obamas, 'sentiments_obama')

    print('Average positivity in Trump\'s tweets:', end=" ")
    print(positivity(trumps))
    print('Average positivity in Obama\'s tweets:', end=" ")
    print(positivity(obamas))

    print('Average negativity in Trump\'s tweets:', end=" ")
    print(negativity(trumps))
    print('Average negativity in Obama\'s tweets:', end=" ")
    print(negativity(obamas))


    # print(cosine_sim(trumpwords, hillarywords))


if __name__ == '__main__':
    main()
