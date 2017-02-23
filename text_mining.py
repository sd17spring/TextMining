import requests
import re
import string
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Samantha Young

# Getting Harry Potter 1 from archive .org

html1 = BeautifulSoup(requests.get("https://archive.org/stream/Book5TheOrderOfThePhoenix/Book%201%20-%20The%20Philosopher's%20Stone_djvu.txt").text, 'lxml')
html1.find('pre')  # find the story
str(html1.find('pre'))  # the story, as a string. Includes embedded <b> etc.
textfromsite1 = str(re.sub(r'<.+?>', '', str(html1.find('pre')))) #saving the story as a string

# Getting Harry Potter 5 from archive .org

html5 = BeautifulSoup(requests.get("https://archive.org/stream/Book5TheOrderOfThePhoenix/Book%205%20-%20The%20Order%20of%20the%20Phoenix_djvu.txt").text, 'lxml')
html5.find('pre')  # find the first paragraph
str(html5.find('pre'))
textfromsite5 = str(re.sub(r'<.+?>', '', str(html5.find('pre'))))

#H Getting Harry Potter 7 from archive .org

html7 = BeautifulSoup(requests.get('https://archive.org/stream/Book5TheOrderOfThePhoenix/Book%207%20-%20The%20Deathly%20Hallows_djvu.txt').text, 'lxml')
html7.find('pre')  # find the first story
str(html7.find('pre'))
textfromsite7 = str(re.sub(r'<.+?>', '', str(html7.find('pre')))) #saving the story as a string


def load_text_convert(st):
    #makes string a list that is usable in rest of functions
    exclude = set(string.punctuation) # makes set of punctuation characters
    titles = ["Philosophers", "Stone", "Order", "Phoenix", "Deathly", "Hallows", "Rowling"] # list of words in titles
    s = ''.join(ch for ch in st if ch not in exclude) # for each character of the story creates a new string without any of the pucntiation
    harList = s.split() #breaks up string at the spaces creates a list of elements
    harList2 = [element for element in harList if (len(element) > 4 and (element not in titles))] #only inlcudes words longer than 4 characters and not in the title
    return harList2


def analyze_Sentiment(fi):
    # needs a str or a file no lists
    #makes dictionary of sentiment
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(fi)


def word_Frequency(fi):
    word_freq = dict()
    for c in fi:
        word_freq[c] = word_freq.get(c, 0) + 1  #counts the number of times eeach word appears and keeps track in dictioary
    return word_freq


def top_10(f1):
    #finds top 10 words used
    f1_words = word_Frequency(f1)
    f1sorted = sorted(f1_words, key=f1_words.__getitem__, reverse=True) # sorts dictionary by value (by frequency of word in story) highest value first
    f1sorted = f1sorted[:10] #returns the first 10 words
    print(f1sorted)


def least_frequent_10(f1):
    #finds top 10 words not used
    f1_words = word_Frequency(f1)
    f1sorted = sorted(f1_words, key=f1_words.__getitem__)# sorts dictionary by value (by frequency of word in story)
    f1sorted = f1sorted[:10] #returns the first 10 words
    print(f1sorted)


def average_Length(fi, name):
    #computes teh average length of all the words in teh story
    sum = 0
    for c in fi:
        sum = sum + len(c) #adds the length of every word in the text
    print("average word length of %s is" %(name)) # divides it by number of words  in text
    return sum / len(fi)


def compare_average_Length(tx1, tx2):
    #finds the difference between averages between 2 works
    text1av = average_Length(tx1, "text1")
    text2av = average_Length(tx2, "text 2")
    dif = text2av - text1av # takes difference of
    print("the difference in average word length of text 1 and 2 is")
    return dif

#commented out becasue they take a really long time to run
# analyze_Sentiment(textfromsite5)
# analyze_Sentiment(textfromsite1)
# analyze_Sentiment(textfromsite7)
text7 = load_text_convert(textfromsite7)
text5 = load_text_convert(textfromsite5)
text1 = load_text_convert(textfromsite1)

print("Book 1")
print(average_Length(text1, "Philospher's Stone"))
print("Most Frequent:")
top_10(text1)
print ("Least Frequent:")
least_frequent_10(text1)

print("Book 5")
print(average_Length(text5, "Order of The Phoenix"))
print("Most Frequent:")
top_10(text5)
print ("Least Frequent:")
least_frequent_10(text5)

print("Book 7")
print(average_Length(text7, "Deathly Hallows"))
print("Most Frequent:")
top_10(text7)
print ("Least Frequent:")
least_frequent_10(text7)
