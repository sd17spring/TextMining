import requests
import nltk
import operator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter


papers = ['fedpaper1.txt', 'fedpaper2.txt', 'fedpaper3.txt', 'fedpaper4.txt', 'fedpaper5.txt', 'fedpaper6.txt', 'fedpaper7.txt', 'fedpaper8.txt', 'fedpaper9.txt', 'fedpaper10.txt']


def fed_paper_creator():
    '''
    This function writes the lines from each one of the first 10 Federalist Papers to a corresponding
    text file. It makes the words into one string, and makes them all lowercase
    '''
    input_file = open("fedpapers.txt", "r")
    lines = input_file.readlines()

    paper1 = str.lower(' '.join(lines[32:194]))
    paper2 = str.lower(' '.join(lines[196:370]))
    paper3 = str.lower(' '.join(lines[372:535]))
    paper4 = str.lower(' '.join(lines[537:708]))
    paper5 = str.lower(' '.join(lines[710:857]))
    paper6 = str.lower(' '.join(lines[859:1108]))
    paper7 = str.lower(' '.join(lines[1110:1339]))
    paper8 = str.lower(' '.join(lines[1341:1551]))
    paper9 = str.lower(' '.join(lines[1553:1762]))
    paper10 = str.lower(' '.join(lines[1764:2064]))

    lines = [paper1, paper2, paper3, paper4, paper5, paper6, paper7, paper8, paper9, paper10]
    papers = ['fedpaper1.txt', 'fedpaper2.txt', 'fedpaper3.txt', 'fedpaper4.txt', 'fedpaper5.txt', 'fedpaper6.txt', 'fedpaper7.txt', 'fedpaper8.txt', 'fedpaper9.txt', 'fedpaper10.txt']

    for i in range(len(lines)):
        file = open(papers[i], 'w')
        file.write(lines[i])
        file.close()


def paper_split(paper):
    '''
    This function tokenizes each one of the Federalist Papers. It removes punctuation, spaces, and about 25 of the most common words according to Wikipedia.
    '''
    tokenpaper = open(paper).read()
    words = nltk.word_tokenize(tokenpaper)
    '''common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'do']
    common_words2 = ['at', 'this', 'but', 'by', 'from']'''
    for word in words:
        if word == '.' or word == ';' or word == ':' or word == ',' or word == '-' or word == '!' or word == '"' or word == '?' or word == '(' or word == ')':
            words.remove(word)
        if word == "'" or word == '[' or word == ']' or word == "'\\n" or word == '--':
            words.remove(word)
        '''if word in common_words or word in common_words2:
            words.remove(word)
        if word == 'the' or word == 'a':
            words.remove(word)'''
    return words
    print(words)


def new_paper(papers):
    '''
    This function writes the new tokenized words into the old text file.
    '''
    fed_paper_creator()
    for paper in papers:
        words = paper_split(paper)
        wordstr = str(words)
        file = open(paper, 'w')
        file.write(wordstr)
        file.close()
        return words


def word_frequency(papers):
    '''
    This function counts the frequency of the words in the Federalist papers
    '''
    words = new_paper(papers)
    d = dict()
    for word in words:
        frequency = d.get(word, 0)
        d[word] = frequency + 1
    return d


def sort_frequencies(papers):
    '''
    This function sorts the frequencies in decreasing order.
    '''
    d = word_frequency(papers)
    freq_sort = sorted(d.items(), reverse=True, key=operator.itemgetter(1))
    return freq_sort


def sentiment():
    '''
    This function analyzes and averages the sentiment of the first 10 papers by author
    '''
    fed_paper_creator()
    input_file = open("fedpapers.txt", "r")
    lines = input_file.readlines()

    analyzer = SentimentIntensityAnalyzer()

    sent1 = analyzer.polarity_scores(str(' '.join(lines[32:194])))
    sent2 = analyzer.polarity_scores(str(' '.join(lines[196:370])))
    sent3 = analyzer.polarity_scores(str(' '.join(lines[372:535])))
    sent4 = analyzer.polarity_scores(str(' '.join(lines[537:708])))
    sent5 = analyzer.polarity_scores(str(' '.join(lines[710:857])))
    sent6 = analyzer.polarity_scores(str(' '.join(lines[859:1108])))
    sent7 = analyzer.polarity_scores(str(' '.join(lines[1110:1339])))
    sent8 = analyzer.polarity_scores(str(' '.join(lines[1341:1551])))
    sent9 = analyzer.polarity_scores(str(' '.join(lines[1553:1762])))
    sent10 = analyzer.polarity_scores(str(' '.join(lines[1764:2064])))

    '''Hamilton'''
    sumHam = dict(Counter(sent1) + Counter(sent6) + Counter(sent7) + Counter(sent8) + Counter(sent9))
    meanHam = {k: sumHam[k] / float((k in sent1) + (k in sent6) + (k in sent7) + (k in sent8) + (k in sent9)) for k in sumHam}
    print('Alexander Hamilton wrote Federalist Papers 1 and 6-9. This the average sentiment of those papers: ', meanHam)
    '''Jay'''
    sumJay = dict(Counter(sent2) + Counter(sent3) + Counter(sent4) + Counter(sent5))
    meanJay = {k: sumJay[k] / float((k in sent2) + (k in sent3) + (k in sent4) + (k in sent5)) for k in sumJay}
    print('John Jay wrote Federalist Papers 2-5. This the average sentiment of Papers 2-5: ', meanJay)
    '''Madison'''
    print('James Madison wrote Federalist Paper 10. This the average sentiment of Paper 10: ', sent10)


print(sort_frequencies(papers))


print(sentiment())
