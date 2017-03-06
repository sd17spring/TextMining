import wikipedia
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

def wikiInfo():
    """
        Originally worked with wikipedia to look at online text

        returns: tuple of text strings from wikipedia articles
    """

    # finds the pages
    cat = wikipedia.page("Cat")
    dog = wikipedia.page("Dog")

    # saves the content of the pages as strings
    catInfo = cat.content
    dogInfo = dog.content

    # returns tuple of the full text strings
    return catInfo, dogInfo

def getBook():
    """
        After plaing with wikipedia I moved to Project Gutenberg

        returns: tuple of text strings from txt links from Project Gutenberg
    """

    # take the txt documents from Project Gutenberg
    japaneseft = requests.get(
    'http://www.gutenberg.org/cache/epub/4018/pg4018.txt').text

    indianft = requests.get(
    'http://www.gutenberg.org/files/7128/7128-0.txt').text

    americanft = requests.get(
    'http://www.gutenberg.org/cache/epub/4357/pg4357.txt').text

    # returns tuple of the full text strings
    return japaneseft, indianft, americanft

def sent(info):
    """
        Find the sentiments of string info
        Uses vader for sentiment analysis

        return: sentiment analysis of info
    """

    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(info)

def topTen(info):
    """
        Finds the top ten words of string info

        returns: top ten words of info
    """

    # split string into list of words
    infoList = info.split()

    # removes characters from beginning and ending of words, goes through list
    stripped = []
    for word in infoList:
        word = word.lower()
        stripped.append(word.strip(" /.,?!':;[]\")(%\r\n"))

    # creates a frequency histogram dictionary of the words in stripped
    hist = dict()
    for c in stripped:
        hist[c] = hist.get(c, 0) + 1

    # converts the histogram dictionary into a list of tuples
    listHist = []
    for key in hist:
        listHist.append((key, hist[key]))

    # modifies listHist to sort it from most frequent to least frequent
    sort = sorted(listHist, key=lambda words: words[1], reverse=True)

    # list of words I want to remove form histList
    unwanted = ['a', 'an', 'be', 'and', 'are', 'from', 'for', 'the', 'they',
    'their', "they're", 'then', 'them', 'is', 'if', 'of', 'with', 'to', 'in',
    'was', 'that', 'as', 'at', 'this', 'so', 'had','on']

    # removes unwanted words from listHist, creates new list
    wanted = [word for word in sort if word[0] not in unwanted]

    # finds the top ten words
    top = wanted[:10]

    # returns top ten
    return top

def main():
    """
        Main function to call functions and print
    """
    japaneseft, indianft, americanft = getBook()
    print(topTen(japaneseft))
    print(topTen(indianft))
    print(topTen(americanft))
    print(sent(japaneseft))
    print(sent(indianft))
    print(sent(americanft))


if __name__ == "__main__":
    main()
