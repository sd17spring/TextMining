import random, pickle, string, nltk, numpy, os
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def open_file(filename):
    input_file = open(filename,'br') #open syntax uses the file name and mode "br" so we have binary and reading mode
    tweets = pickle.load(input_file) #taking tweets from pickle and loading into input file
    input_file.close()
    return tweets

##getting tweets, looking at each word to valiate it's a word and adding it to dictionary
def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """

    hist = {}
    if filename[-7:] == '.pickle': #looking to see if it's a pickle file
        raw_data = open_file(filename)

        #analyzing by line
        for line in raw_data:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            #analyze by letter
            for word in line.split():
                # remove punctuation and convert to lowercase
                word = word.strip(strippables)
                word = word.lower()

                # update the histogram where it will count the words is in the dictionary
                #and if it is then the +1 will be added associated to the key
                hist[word] = hist.get(word, 0) + 1
        return hist

    else:
        fp = open(filename, encoding='utf8')
        for line in fp:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            for word in line.split():
                # remove punctuation and convert to lowercase
                word = word.strip(strippables)
                word = word.lower()

                # update the histogram
                hist[word] = hist.get(word, 0) + 1

        return hist


#comparing 2 dictionaries - comparing a histogram and a list of actual words (think:Webster dictionary)
#to reference which words actually exist in the english dictionary. Removing fake words.
def similar(d1, d2):
    """Returns a dictionary with all keys that appear in d1 and d2.

    d1, d2: dictionaries
    """
    result = dict()
    for i in d1:
        if i in d2:
            result[i] = d1[i]
    return result

#removing words that don't help w/ sentiment
def finalized_words(x):
    """
    Returns a list of words that have the stop words removed that have been stemmed given a dictionary

    x is a dictionary
    returns a dictionary
    """

    st = LancasterStemmer() #stems the word walking turns to 'walk'
    stop = set(stopwords.words('english')) #removes words like 'this, is, and, a for'
    result = {}

    for i in x:
        #Check to see if the word is a stopword. If it is not a stopword, then append it to list
        if i not in stop:
            stemmed_word = st.stem(i)
            result[stemmed_word] = x[i]
        #Stem the words
    return result

#specifying common words by specifying the 'num' of most common words within tweets
def most_common(hist, num):
    """Makes a list of word-freq pairs in descending order of frequency.

    num: the number of results to see.

    hist: map from word to frequency

    returns: list of num (frequency, word) pairs
    """
    #making histogram that will pull out the word and the # of frequency it appears
    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))

    temp.sort()
    temp.reverse()
    return temp[:num]

def write_file(hist, filename):
    '''
    Writes a dictionary to a pickle file.
    filename: string without extension
    hist: dictionary
    '''
    filename += '.pickle'


    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(hist,f)
        f.close()
        print('File created as %s.' % filename)
    else:
        response = input("File %s already exists. Replace existing? (Y/N):    " % filename)
        if response.lower() == 'y':
            f = open(filename,'wb')
            pickle.dump(hist,f)
            f.close()
            print('File replaced as %s.' % filename)
        elif response.lower() == 'n':
            print('Action aborted.')

def main():
    input_file1 = open('obamatweets.pickle','br')
    raw_data1 = pickle.load(input_file1)

    hist1 = process_file('obamatweets.pickle')
    words = process_file('words.txt')

    real_words1 = similar(hist1, words)
    completed_words1 = finalized_words(real_words1)

    print("\n\nThe tokenized words in the Obama tweets are:")
    print(completed_words1)

    # write_file(completed_words1, 'tokenizedObama')

    input_file2 = open('trumptweets.pickle','br')
    raw_data2 = pickle.load(input_file2)

    hist2 = process_file('trumptweets.pickle')

    real_words2 = similar(hist2, words)
    completed_words2 = finalized_words(real_words2)

    print("\n\nThe tokenized words in the Trump tweets are:")
    print(completed_words2)

    print('Most common words in Obama\'s tweets are:')
    print(most_common(completed_words1, 10))
    print('Most common words in Trump\'s tweets are:')
    print(most_common(completed_words2, 10))



if __name__ == '__main__':
    main()
