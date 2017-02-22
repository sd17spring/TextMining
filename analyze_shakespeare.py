import pickle
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


common_words = ['i', 'what', 'the', 'at', 'why', 'o', 'that',
                'and', 'to', 'is', 'a', 'of', 'in', 'my', 'with', 'not',
                'but', 'thou', 'this', 'for', 'it', 'be', 'as', 'thy', 'so',
                'thee', 'have', 'shall', 'me', 'you', 'by', 'from', 'if',
                'she', 'him', 'he', 'hers', 'his', 'will', 'your', 'lord']

romeo_characters = ['Rom', 'Jul', 'Nurse', 'Tyb', 'Ben', 'Par', 'Friar']
ham_characters = ['Ham', 'Oph', 'Hor', 'Ros', 'Guil', 'Pol', 'Laer']


def load_romeo():
    """
    Loads text from pickled text file and cuts off the stuff
    at the beginning that's not important
    """
    input_file = open('romeo.txt', 'rb')
    loaded_text = pickle.load(input_file)
    loaded_text_truncated = loaded_text[loaded_text.find('SCENE'):]
    return loaded_text_truncated


def load_hamlet():
    """
    Loads text from pickled text file and cuts off the stuff
    at the beginning that's not important
    """
    input_file = open('hamlet.txt', 'rb')
    loaded_text = pickle.load(input_file)
    loaded_text_truncated = loaded_text[loaded_text.find('SCENE'):]
    return loaded_text_truncated


def edit_text(words):
    """
    Takes text, gets rid of punctuation, makes lowercase,
    and gets rid of whitespace character \r. Returns list
    of all words
    >>> edit_text('HI THERE!!! You are so $WEET?')
    ['hi', 'there', 'you', 'are', 'so', 'weet']
    """
    for symbol in string.punctuation:  # removes punctuation
        words = words.replace(symbol, '')
    edited_words = words.replace('\r', '')  # removes whitespace character

    edited_words = edited_words.lower()  # changes all words to lowercase
    final_edit = edited_words.split()  # splits words into list
    return final_edit


def word_frequencies(text):
    """
    Counts frequency of each word, returns top 10 most
    frequent words not including some common words
    """
    # Make word histogram
    histogram = dict()
    for word in text:
        histogram[word] = histogram.get(word, 0) + 1

    # Make List from most frequent to least frequent
    t = []
    for key, value in histogram.items():
        t.append((value, key))
    t.sort(reverse=True)

    # Remove Common Words
    for i in range(10):
        for element in t:
            if element[1] in common_words:
                del t[t.index(element)]

    top10 = t[:10]  # only includes top 10 items
    return top10


def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)


def character_text(text, character):
    """
    finds all the dialogue for one certain character in either
    Romeo and Juliet or Hamlet
    """
    all_dialogue = ''

    # find start/end based on which play it is
    # speaker start marked by . and then newlines mark end of dialogue
    if character in romeo_characters:
        start = text.find(character + '. ')
        end = text[start:].find('\r\n\r\n')
    else:
        start = text.find(character + '.\r\n')
        end = text[start:].find('\r\n\r\n')

    # if can't find it, return empty string
    if start == -1 or end == -1:
        return ''

    # add new bit of dialogue to all dialogue
    all_dialogue += (text[start:start+end])

    # do again but after the end of this piece of dialogue
    all_dialogue += (character_text(text[start+end:], character))
    return all_dialogue


def analyze_all_characters(characters, play_text):
    """
    Analyzes the sentiment for the characters given and
    also finds the top 10 most frequent words for that character
    """

    data = dict()
    for character in characters:
        text = character_text(play_text, character)  # isolate dialogue
        sentiment = analyze_sentiment(text)
        most_common_words = word_frequencies(edit_text(text))
        data[character] = sentiment, most_common_words
    return data


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    print(analyze_all_characters(romeo_characters, load_romeo()))
    print(analyze_all_characters(ham_characters, load_hamlet()))
