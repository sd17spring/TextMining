import matplotlib.pyplot as plt
import pickle


def unpickle(pickledItem):
    return(pickle.load(open(pickledItem, 'rb')))

def getScores(table):
    return [table['pos'], table['neg'], table['neu']]


if __name__ == '__main__':

    scores = unpickle('scores.pickle')

    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['yellowgreen', 'lightcoral', 'gold']
    scoresOW = getScores(scores[0])
    scoresOC = getScores(scores[1])
    scoresTW = getScores(scores[2])
    scoresTC = getScores(scores[3])

    plt.subplot(221)
    plt.pie(scoresOW, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Obama: Wikipedia')

    plt.subplot(222)
    plt.pie(scoresOC, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Obama: Conservapedia')

    plt.subplot(223)
    plt.pie(scoresTW, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Trump: Wikipedia')

    plt.subplot(224)
    plt.pie(scoresTC, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Trump: Conservapedia')

    plt.show()
