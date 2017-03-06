import wikipedia
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def wikiInfo():
    cat = wikipedia.page("Cat")
    dog = wikipedia.page("Dog")

    catInfo = cat.content
    dogInfo = dog.content

    return catInfo, dogInfo

def sent(info):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(info)

def topTen(info):
    infoList = info.split()

    stripped = []
    for word in infoList:
        stripped.append(word.strip("/.,?'':;[]"")(%"))

    hist = dict()
    for c in stripped:
        hist[c] = hist.get(c, 0) + 1

    listHist = []
    for key in hist:
        listHist.append((key, hist[key]))

    return sorted(listHist, key=lambda words: words[1], reverse=True)


    unwanted = ['a', 'an', 'be', 'and', 'are', 'from', 'for', 'the', 'they',
    'their', "they're", 'then', 'them', 'is', 'if', 'of', 'with']



if __name__ == "__main__":
    cat, dog = wikiInfo()
    print(sent(cat))
    print(sent(dog))
    print(topTen(cat))
