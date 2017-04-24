import pickle
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyzer(filename):
    input_file = open(filename, 'rb')
    websitee = pickle.load(input_file)

    soup = BeautifulSoup(websitee, "html.parser")

    text = soup.get_text()
    count = 0
    newtext = text.split()
    for i in newtext:
        if(i == "trump" or i == "Trump"):
            count += 1
    analyze = SentimentIntensityAnalyzer()
    scores = analyze.polarity_scores(text)
    return count, scores


if __name__ == "__main__":
    websites = ['bbc.pickle', 'cnn.pickle', 'foxnews.pickle']
    for i in websites:
        count = analyzer(i)[0]
        scores = analyzer(i)[1]
        print("Number of times Trump is mentioned: " , count)
        print("Positivity/Negativity score: ", scores)
