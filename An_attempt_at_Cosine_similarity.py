import requests
import pickle
import string
import urllib
#s wikipedia
#from bs4 import BeautifulSoup
#import urllib2
#import urllib


def load_pickles():
    communist_manifesto = requests.get('http://www.gutenberg.org/files/23905/23905-readme.txt').text
    #print(oliver_twist_full_text)

    print(communist_manifesto)

    f = open('communist_manifesto.pickle','wb')
    pickle.dump(communist_manifesto,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('communist_manifesto.pickle','rb')
    reloaded_copy_of_texts1 = pickle.load(input_file)

    constitution = requests.get('http://www.gutenberg.org/cache/epub/5/pg5.txt').text
    #print(oliver_twist_full_text)

    f = open('constitution.pickle','wb')
    pickle.dump(constitution,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('constitution.pickle','rb')
    reloaded_copy_of_texts2 = pickle.load(input_file)

    nietzsche = requests.get('http://www.gutenberg.org/cache/epub/5/pg5.txt').text
    #print(oliver_twist_full_text)

    f = open('nietzsche.pickle','wb')
    pickle.dump(nietzsche,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('nietzsche.pickle','rb')
    reloaded_copy_of_texts3 = pickle.load(input_file)

    ethics = requests.get('http://www.gutenberg.org/cache/epub/8438/pg8438.txt').text
    #print(oliver_twist_full_text)

    f = open('ethics.pickle','wb')
    pickle.dump(ethics,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('ethics.pickle','rb')
    reloaded_copy_of_texts4 = pickle.load(input_file)

    utilitarianism = requests.get('http://www.gutenberg.org/cache/epub/11224/pg11224.txt').text
    #print(oliver_twist_full_text)

    f = open('utilitarianism.pickle','wb')
    pickle.dump(utilitarianism,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('utilitarianism.pickle','rb')
    reloaded_copy_of_texts = pickle.load(input_file)


"""
html = BeautifulSoup(requests.get("http://www.worldfuturefund.org/Reports2013/hitlerenablingact.htm").text, 'lxml')
html.find('p')
str(html.find('p'))

html1 = BeautifulSoup(requests.get("https://www.marxists.org/reference/archive/stalin/works/1941/11/07.htm").text, 'lxml')
html1.find('p')
str(html1.find('p'))

html2 = BeautifulSoup(requests.get("http://www.politico.com/story/2016/07/full-transcript-donald-trump-nomination-acceptance-speech-at-rnc-225974").text, 'lxml')
html2.find('p')
str(html2.find('p'))

html3 = BeautifulSoup(requests.get("http://obamaspeeches.com/").text, 'lxml')
html3.find('p')
str(html3.find('p'))

url = "http://www.worldfuturefund.org/Reports2013/hitlerenablingact.htm"
content = urllib2.urlopen(url)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
analyzer.polarity_scores('Software Design is my favorite class!')

"""
def process_file(name_of_file):
    hist = dict()
    open_file = open(name_of_file, 'rb')
    for l in open_file:
        process_line(l,hist)
    return hist

def process_line(line,hist):
    # line = line.replace('-', ' ')

    for word in line.split():
        # word = word.strip(string.punctuation + string.whitespace) #TODO y no work
        word = word.lower()
        hist[word]=hist.get(word,0)+1

constitution_hist = process_file('constitution.pickle')
ethics_hist = process_file('ethics.pickle')
communist_manifesto_hist = process_file('communist_manifesto.pickle')
nietzsche_hist = process_file('nietzsche.pickle')
utilitarianism_hist = process_file('utilitarianism.pickle')

#the inverse function takes a dictionary and returns a list of tuples that are sorted by frequency and word.
"""def inverse(dictionary):
    inverse_list = []
    for key in (dictionary):
        if dictionary[key] > 20:
            t=(dictionary[key]/(len(dictionary)),key)
            inverse_list.append(t)
    new_list = sorted(inverse_list)
    return new_list"""

# Looks at the frequency of a word in a document and makes a list of tuples that have a frequency greater than 20
def frequency(dictionary):
    frequency_list = []
    for key in (dictionary):
        if dictionary[key] > 20:
            t=(key,(dictionary[key]/(len(dictionary))))
            frequency_list.append(t)
    return frequency_list


#finding the similarities of words between two lists
"""def comparing(list1,list2):
    new_list1=[]
    new_list2=[]
    for i in list1:
        for j in list2:
            if i[1] == j[1]:
                new_list1.append(i)
                new_list2.append(j)
    return new_list1, new_list2

data=comparing(util,commie)

def unique(list1,list2):
    new_list1=[]
    new_list2=[]
    for i[1] in list1:
        for i[1] not in list2:
            new_list1.append(i)
    for j[1] in list2:
        for j[1] not in list1:
            new_list2.append(j)
    return new_list1, new_list2"""

#finds the amount of documents that the word appears in (for 3 documents)
def IDF(dictionary):
    amount_of_docs_with_word = []
    print(dictionary)
    for key in (dictionary):
        print(key)
        a = 0
        for j in ethics_hist:
            if key[0]==j[0]:
                a=+ 1
        for k in nietzsche_hist:
            if key[0]==k[0]:
                a=+ 1
        for l in utilitarianism_hist:
            if key[0]==l[0]:
                a=+ 1
        t = (dictionary[key],a)
        amount_of_docs_with_word.append(t)
    return amount_of_docs_with_word


def TF_IDF(dictionary):
    tf = frequency(dictionary)
    to_solve_idf = IDF(dictionary)
    list_of_tfidf = []
    for key in tf: # for the word that is in both lists
        if key in to_solve_idf:
            true_tf = tf[key]
            true_idf = 1+ math.log(3/to_solve_idf[key]) #solving for the IDF by taking the value of the dict and taking the log of the amount of docs divided by the amount who have the word
            tf_idf_solved = true_tf*true_idf # multiplying the IDF and TF together
            t = (dictionary[key],tf_idf_solved)
            list_of_tfidf.append(t)
    return list_of_tfidf #returning a list of tuples with TF_IDF and word

def prep_for_cosine(dict1, dict2):
    list1 = TF_IDF(dict1)
    list2 = TF_IDF(dict2)
    list_of_similarities= []
    list1_tfidt=[]
    list2_tfidt=[]
    for i[0] in list1:
        if i[0] in list2:
            t=(list1[i[1]], list2[i[1]])
            list_of_similarities.append(t)
            list1_tfidt.append((list1[i[1]])**2)
            list2_tfidt.append((list2[i[1]])**2)
    return list_of_similarities, list1_tfidt, list2_tfidt # returns a list of the tuples that are the elements of the vectos that will be multiplied together

#finds the cosine similarity of the two docs
def cosine_similarity(dict1,dict2):
    list_of_similarities, list1_tfidt, list2_tfidt= prep_for_cosine(dict1, dict2)
    mag_of_list1 = math.sqrt(sum(list1_tfidt))
    mag_of_list2= math.sqrt(sum(list2_tfidt))
    a = 0
    for i in list_of_similarities:
        a = a + i[0]*i[1]
    cosine_sim = a / (mag_of_list1*mag_of_list2)
    return cosine_sim

if __name__ == '__main__':
    load_pickles()
    # cosine_similarity(constitution_hist,communist_manifesto_hist)
