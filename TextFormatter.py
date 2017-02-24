import pickle
from bs4 import BeautifulSoup
import re


def getTextFromHtml(html):
    bshtml = BeautifulSoup(html, 'lxml')
    bshtmlp = bshtml.findAll('p')  # get paragraphs of text only
    text = ''
    for paragraph in bshtmlp:
        newParagraph = paragraph.getText()  # remove HTML from paragraph
        text += newParagraph
        text += '\n'
    text = str(re.sub(r'\[([0-9]+)\]', '', text))  # remove Wikipedia sites
    return text


def unpickle(pickledItem):
    return(pickle.load(open(pickledItem, 'rb')))


def repickle(itemToPickle, fileName):
    f = open(fileName, 'wb')
    pickle.dump(itemToPickle, f)
    f.close


def repickleAsCleanText(pickledItem, fileName):
    rawHtml = unpickle(pickledItem)
    cleanText = getTextFromHtml(rawHtml)
    repickle(cleanText, fileName)


if __name__ == '__main__':

    repickleAsCleanText('obamaWik.pickle', 'obamaWikClean.pickle')
    repickleAsCleanText('obamaCon.pickle', 'obamaConClean.pickle')
    repickleAsCleanText('trumpWik.pickle', 'trumpWikClean.pickle')
    repickleAsCleanText('trumpCon.pickle', 'trumpConClean.pickle')

    # print(obamaWikText)
    # print('------------------------------------------------------------------')
    # print(obamaConText)
    # print('------------------------------------------------------------------')
    # print(trumpWikText)
    # print('------------------------------------------------------------------')
    # print(trumpConText)
