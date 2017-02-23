import requests
import pickle
import string
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#importing all the books:
communist_manifesto = requests.get('http://www.gutenberg.org/cache/epub/61/pg61.txt').text
f = open('communist_manifesto.pickle','wb')
pickle.dump(communist_manifesto,f)
f.close()
input_file = open('communist_manifesto.pickle','rb')
reloaded_copy_of_texts1 = pickle.load(input_file)

constitution = requests.get('http://www.gutenberg.org/cache/epub/5/pg5.txt').text
f = open('constitution.pickle','wb')
pickle.dump(constitution,f)
f.close()
input_file = open('constitution.pickle','rb')
reloaded_copy_of_texts2 = pickle.load(input_file)

trotsky = requests.get('http://www.gutenberg.org/cache/epub/38982/pg38982.txt').text
f = open('trotsky.pickle','wb')
pickle.dump(trotsky,f)
f.close()
input_file = open('trotsky.pickle','rb')
reloaded_copy_of_texts3 = pickle.load(input_file)

utilitarianism = requests.get('http://www.gutenberg.org/cache/epub/11224/pg11224.txt').text
f = open('utilitarianism.pickle','wb')
pickle.dump(utilitarianism,f)
f.close()
input_file = open('utilitarianism.pickle','rb')
reloaded_copy_of_texts5 = pickle.load(input_file)

#analyzes and contrasts sentiments of texts
def analyzing_sentiment():
    analyzer = SentimentIntensityAnalyzer()
    print(analyzer.polarity_scores(reloaded_copy_of_texts1))
    print(analyzer.polarity_scores(reloaded_copy_of_texts2))
    print(analyzer.polarity_scores(reloaded_copy_of_texts3))
    print(analyzer.polarity_scores(reloaded_copy_of_texts5))

#plotting neutral sentiment: bar graph (looked up online)
def making_graphs_neutral():
    objects = ('Communist Manifest','Constitution','Trotsky','Utilitarianism')
    y_pos = np.arange(len(objects))
    performance = [.824,.836,.79,.747]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Neutral Sentiment Ratio')
    plt.title('Neutral Sentiment')
    plt.show()
    plt.savefig("sentiment_neutral.png")

#same for positive sentiment
def making_graphs_pos():
    objects = ('Communist Manifest','Constitution','Trotsky','Utilitarianism')
    y_pos = np.arange(len(objects))
    performance = [.096,.11,.1,.159]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Positive Sentiment Ratio')
    plt.title('Positive Sentiment')
    plt.show()
    plt.savefig("sentiment_pos.png")

#same as well for negative sentiment
def making_graphs_neg():
    objects = ('Communist Manifest','Constitution','Trotsky','Utilitarianism')
    y_pos = np.arange(len(objects))
    performance = [.08,.054,.11,.094]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Negative Sentiment Ratio')
    plt.title('Negative Sentiment')
    plt.show()
    plt.savefig("sentiment_neg.png")

#making_graphs_pos()
#making_graphs_neg()
#making_graphs_neutral()

"""
Results of the sentiment analysis:
{'compound': 0.9998, 'neu': 0.824, 'neg': 0.08, 'pos': 0.096}
{'compound': 0.9999, 'neu': 0.836, 'neg': 0.054, 'pos': 0.11}
{'compound': -1.0, 'neu': 0.79, 'neg': 0.11, 'pos': 0.1}
{'compound': 1.0, 'neu': 0.747, 'neg': 0.094, 'pos': 0.159}"""

#processing each of the files and making a histogram out of them
def process_file(name_of_file):
    hist = dict()
    open_file = open(name_of_file, 'rb')
    for l in open_file:
        process_line(l,hist)
    return hist

def process_line(line,hist):
    #line = line.replace('-', ' ')
    for word in line.split():
        #word = word.strip(string.punctuation + string.whitespace) #TODO y no work
        word = word.lower()
        hist[word]=hist.get(word,0)+1

#processing each of the pickled texts
constitution_hist = process_file('constitution.pickle')
communist_manifesto_hist = process_file('communist_manifesto.pickle')
trotsky_hist = process_file('trotsky.pickle')
utilitarianism_hist = process_file('utilitarianism.pickle')

#eliminates any word shorter than b and then determines the most common words of a dictionary (n amount)
def top_words(dictionary,n,b):
    """
    >>> top_words({'cat':1,'dog':1,'elephant':5,'soul':10,'jazz':20},3,2)
    [(5, 'elephant'), (10, 'soul'), (20, 'jazz')]
    """
    inverse_list = []
    cool_dict =[]
    for key in (dictionary):
        t=(dictionary[key],key)
        inverse_list.append(t)
    for i in inverse_list:
        if len(i[1]) > b:
            cool_dict.append(i)
    new_list = sorted(cool_dict)
    #print(new_list[len(cool_dict)-n:])
    return new_list[len(cool_dict)-n:]

#determine the words that are unique to each text (and that are the most common words)
def unique_words(a,b,c,d):
    """Examples:
    >>> unique_words(['a','cat','dog'],['a','elephant','fish'],['fish','pet','car'],['a','truck','car'])
    (['cat', 'dog'], ['elephant'], ['pet'], ['truck'])
    """
    a_list_words=[]
    b_list_words=[]
    c_list_words = []
    d_list_words = []
    for i in a:
        if i not in b:
            if i not in c:
                if i not in d:
                    a_list_words.append(i)
    for j in b:
        if j not in a:
            if j not in c:
                if j not in d:
                    b_list_words.append(j)
    for k in c:
        if k not in a:
            if k not in b:
                if k not in d:
                    c_list_words.append(k)
    for l in d:
        if l not in a:
            if l not in b:
                if l not in c:
                    d_list_words.append(l)
    return a_list_words,b_list_words,c_list_words,d_list_words

def most_common_words(a,b,d,e,n,h):
    """
    >>> most_common_words({'a':5,'cat':10,'dog':10,'fish':2},{'a':10,'elephant':20,'fish':20,'car':2},{'fish':20,'pet':20,'car':10,'love':5},{'a':20,'truck':20,'truck':20,'death':2},3,2)
    (['cat', 'dog'], ['elephant'], ['pet'], ['truck'])
    """
    a_new =[]
    b_new=[]
    c_new =[]
    d_new=[]
    a_list = top_words(a,n,h)
    b_list = top_words(b,n,h)
    #c_list = top_words(c,5)
    d_list = top_words(d,n,h)
    e_list = top_words(e,n,h)
    for i in a_list:
        a_new.append(i[1])
    for h in b_list:
        b_new.append(h[1])
    for k in d_list:
        c_new.append(k[1])
    for l in e_list:
        d_new.append(l[1])
    #print(a_list,b_list)
    return unique_words(a_new,b_new,c_new,d_new)
    #returns a list of the lists of top n words

print(most_common_words(constitution_hist,communist_manifesto_hist,trotsky_hist,utilitarianism_hist,50,3))


if __name__ == "__main__":
    import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(most_common_words, globals(),verbose = True)
