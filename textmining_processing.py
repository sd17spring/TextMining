
import pickle
import string

"""
Finding  the longest word
"""
plays = ['geschwister.txt', 'berlichingen.txt', 'iphigenie.txt']
prose = ['reinekefuchs.txt']
book = ['werther1.txt', 'werther2.txt']


def clean_text(file_name):
    input_file = open(file_name, 'rb')
    text = pickle.load(input_file)
    if file_name in plays:
        start = text.find('Personen')  # beginning of play
    elif file_name in prose:
        start = text.find('Inhalt')  # beginning of prose
    elif file_name in book:
        start = text.find('Ausgabe')  # beginning of prose
    text = text[start:]
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('--', ' ')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace(')', '')
    text = text.replace('(', '')
    text = text.replace("'", '')
    print(file_name)
    return text


def longest_words(text):
    text = text.split()
    # print(text)
    words = []
    for word in text:
        length = len(word)
        words.append((length, word))
        words.sort(reverse=True)
    print(words)
    top = words[0:4]
    return top


def final_analysis(text):
    clean = clean_text(text)
    top = longest_words(clean)
    for pair in top:
        print(pair)


# final_analysis('berlichingen.txt')
final_analysis('geschwister.txt')
# final_analysis('iphigenie.txt')
# final_analysis('reinekefuchs.txt')
# final_analysis('werther1.txt')
# final_analysis('werther2.txt')
