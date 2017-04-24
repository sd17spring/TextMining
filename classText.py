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

        punctuation = [',', ';', '.', '-', '--', '!', '?', ')', '(', "'", '@', '*']
        for mark in punctuation:
            text = text.replace(mark, ' ')

        # Remove the header
        start = text.find('START OF THIS PROJECT GUTENBERG')
        if start == -1:
            start = text.find('END THE SMALL PRINT') + 150  # appox end of the header text

        # Remove the footer
        end = text.find('END OF THIS PROJECT GUTENBERG')
        if end == -1:
            end = text.find('Ende dieses')  # ending statement in German

        # Cut text
        text = text[start:end]

        # remove unwanted punctuation

        return text

    def longestWords(self):
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
    pass
