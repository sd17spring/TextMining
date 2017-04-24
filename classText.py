"""
Sarah Barden
This is a class that creates Text objects for my text mining project.  It
includes two methods called cleanText and longestWords.
"""
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
        """
        Takes a Gutenberg text file and cleans it, removes punctuation, etc.
        Returns the cleaned text as a string
        """
        inputFile = open(self.fileName, 'rb')
        text = pickle.load(inputFile)

        # removing unwanted punctuation
        punctuation = [',', ';', '.', '-', '--', '!', '?', ')', '(', "'", '@', '*']
        for mark in punctuation:
            text = text.replace(mark, ' ')

        # Project Gutenberg text files have a long footer and header in every
        # file. The following finds the end of the header and the start of the
        # footer and removes those sections.
        start = text.find('START OF THIS PROJECT GUTENBERG')
        if start == -1:
            start = text.find('END THE SMALL PRINT') + 150  # approx end of the header text

        end = text.find('END OF THIS PROJECT GUTENBERG')
        if end == -1:
            end = text.find('Ende dieses')  # ending statement in German

        text = text[start:end]  # Cut the text to remove footer/header
        return text

    def longestWords(self, number):
        """
        Takes in a Gutenberg text file and outputs the longest n words, where n
        is an input.  Returns a list of tuples, where each tuple is the length
        of the word and the word as a string
        """

        text = self.cleanText()
        text = text.split()
        words = []
        # After splitting the whole text into a list of words, this sorts them
        # all by the length into a list, from longest to shortest.
        for word in text:
            length = len(word)
            words.append((length, word))
            words.sort(reverse=True)
        top = words[0:number]
        return top


if __name__ == '__main__':
    pass
