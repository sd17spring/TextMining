import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def unpickle(pickledItem):
    return(pickle.load(open(pickledItem, 'rb')))


def repickle(itemToPickle, fileName):
    f = open(fileName, 'wb')
    pickle.dump(itemToPickle, f)
    f.close


def printScores(scores):
    print('Positive: {}  \tNegative: {}  \tNeutral: {}'.format(scores['pos'], scores['neg'], scores['neu']))


if __name__ == '__main__':

    obamaWik = unpickle('obamaWikClean.pickle')
    obamaCon = unpickle('obamaConClean.pickle')
    trumpWik = unpickle('trumpWikClean.pickle')
    trumpCon = unpickle('trumpConClean.pickle')

    analyzer = SentimentIntensityAnalyzer()

    obamaWikScores = analyzer.polarity_scores(obamaWik)
    obamaConScores = analyzer.polarity_scores(obamaCon)
    trumpWikScores = analyzer.polarity_scores(trumpWik)
    trumpConScores = analyzer.polarity_scores(trumpCon)

    repickle([obamaWikScores, obamaConScores, trumpWikScores, trumpConScores], 'scores.pickle')

    print('Obama, Wikipedia:')
    printScores(obamaWikScores)
    print('\nObama, conservapedia:')
    printScores(obamaConScores)
    print('\nTrump, Wikipedia:')
    printScores(trumpWikScores)
    print('\nTrump, conservapedia:')
    printScores(trumpConScores)
