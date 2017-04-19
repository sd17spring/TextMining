# Sarah Barden
# This is a class that creates Text objects for my text mining project
import pickle


class Text:

    def __init__(self, title, author, fileName):
        self.title = title
        self.author = author
        self.fileName = fileName

    def __str__(self):
        string = ''
        string += '{} by {}'.format(self.title, self.author)
        return string

    def cleanText(self):
        inputFile = open(self.fileName, 'rb')
        text = pickle.load(inputFile)
        # find the start/end of the text and remove the header and footer
        start = text.find('START OF THIS PROJECT GUTENBERG')
        if start == -1:
            start = text.find('*END*THE SMALL PRINT') + 150  # end of the header text
        end = text.find('END OF THIS PROJECT GUTENBERG')
        if end == -1:
            end = text.find('Ende dieses')  # ending statement in German
        text = text[start:end]
        # remove unwanted punctuation
        punctuation = [',', '.', '-', '--', '!', '?', ')', '(', "'"]
        for mark in punctuation:
            text = text.replace(mark, ' ')
        return text

    def longest_words(self):
        text = self.cleanText()
        text = text.split()
        words = []
        for word in text:
            length = len(word)
            words.append((length, word))
            words.sort(reverse=True)
        top = words[0:3]
        return top


if __name__ == '__main__':
    # testing
    a = Text('Die Geschwister', 'Johann Wolfgang von Goethe', 'geschwister.txt')
    b = Text('Götz von Berlichingen', 'Johann Wolfgang von Goethe', 'berlichingen.txt')
    c = Text('Iphigenie auf Tauris', 'Johann Wolfgang von Goethe', 'iphigenie.txt')
    d = Text('Reineke Fuchs', 'Johann Wolfgang von Goethe', 'reinekefuchs.txt')
    e = Text('Die Leiden des jungen Werthers 1', 'Johann Wolfgang von Goethe', 'werther1.txt')
    f = Text('Die Leiden des jungen Werthers 2', 'Johann Wolfgang von Goethe', 'werther2.txt')

    yay = [a, b, c, d, e, f]
    for i in yay:
        print(i.longest_words())
