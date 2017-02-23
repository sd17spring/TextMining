import numpy as np
import random

class WordCreator(object):
    def __init__(self, filename=None, wordList=None):
        """
        Initializes variables in WordCreator object
        Creates Transition matrix and normalizes it
        """
        if filename:
            self.txtFile = open(filename, 'r')
            self.wordList = None
        else:
            self.txtFile = None
            self.wordList = wordList
        self.transitions = np.zeros([255, 255])
        self.sumList = []
        self.maxLetters = 0
        self.minLetters = 0
        self.minLetters = self.getMinLetters()
        self.maxLetters = self.getMaxLetters()
        self.setTransitions()

    def getMaxLetters(self):
        """
        Returns the max number of letters in a word in the text file
        """
        currentMax = 0
        if self.txtFile:
            self.txtFile.seek(0)
            for word in self.txtFile:
                if len(word) >= currentMax:
                    currentMax = len(word)
        else:
            for word in self.wordList:
                if len(word) >= currentMax:
                    currentMax = len(word)
        return currentMax

    def getMinLetters(self):
        """
        Returns the minimum number of letters in a word in the text file
        """
        currentMin = 10000
        if self.txtFile:
            self.txtFile.seek(0)
            for word in self.txtFile:
                if len(word) <= currentMin:
                    currentMin = len(word)
        else:
            for word in self.wordList:
                if len(word) <= currentMin:
                    currentMin = len(word)
        return currentMin

    def setTransitions(self):
        """
        Sets the transitions attribute
        Loops through the text file and finds probabilities that
        letters transition into other letters
        Index m, n represents the probability that m transitions to n
        Index 27 represents a space input
        """
        if self.txtFile:
            self.txtFile.seek(0)
            for line in self.txtFile:
                line = line.lower()
                for i in range(len(line)-2):
                    xInd = ord(line[i])
                    yInd = ord(line[i+1])
                    self.transitions[xInd][yInd] += 1
        if self.wordList:
            for line in self.wordList:
                line = line.lower()
                for i in range(len(line)-2):
                    xInd = ord(line[i])
                    yInd = ord(line[i+1])
                    self.transitions[xInd][yInd] += 1
        self.normalizeTransitions()

    def normalizeTransitions(self):
        """
        Adds up a row of transitions and divides it by the sum
        Adds sum to the list of sums (sumList)
        """
        self.sumList = []
        for i in range(len(self.transitions)):
            self.transitions[i], summation = self.norm(self.transitions[i])
            self.sumList.append(summation)

    def norm(self, lst):
        """
        Receives a list (lst) argument
        Normalizes the list
        Returns normalized list and sum of the original entities
        """
        summation = 0
        tempList = self.copyList(lst)
        for i in tempList:
            summation += i
        for i in range(len(tempList)):
            tempList[i] = tempList[i]/summation
        return tempList, summation

    def getSum(self, lst):
        """
        Receives list of numbers
        Returns sum of the list
        """
        summation = 0
        for i in lst:
            summation += i
        return summation

    def copyList(self, lst):
        copy = []
        for i in lst:
            copy.append(i)
        return copy


    def getRanges(self, probList, summation):
            lastVal = 0
            tempList = self.copyList(probList)
            newList = []
            indices = []
            for i in range(len(tempList)):
                if tempList[i]:
                    tempList[i] = tempList[i] * summation
                    newList.append(lastVal + tempList[i])
                    indices.append(i)
                    lastVal += tempList[i]
            return newList, indices


    def getWeightedLetter(self, probList, inSum):
        """
        Receives list of probabilities (probList) and sum of original entities
        of the list
        Generates random letter based on how the letter is weighted in the list
        returns that number
        """
        ranges, indices = self.getRanges(probList, inSum)
        randLetterIndex = random.randint(1, inSum)
        lastVal = 0
        for i in range(len(ranges)):
            if lastVal < randLetterIndex and randLetterIndex <= ranges[i]:
                return chr(indices[i])
            lastVal = ranges[i]

    def genWord(self, n):
        """
        Generates random word based on transition list of length n
        Returns a word (word)
        """
        word = []
        worLen = n
        normList, totalChar = self.norm(self.sumList)
        word.append(self.getWeightedLetter(normList, totalChar))
        for i in range(wordLen-1):
            letterIndex = ord(word[i])
            word.append(self.getWeightedLetter(self.transitions[letterIndex], self.sumList[letterIndex]))
        return ''.join(word)

    def genRandWord(self):
        """
        Generates random word based on transition list
        Returns a word (word)
        """
        wordLen = random.randint(self.minLetters, self.maxLetters)
        word = []
        normList, totalChar = self.norm(self.sumList)
        word.append(self.getWeightedLetter(normList, totalChar))
        for i in range(wordLen-1):
            letterIndex = ord(word[i])
            word.append(self.getWeightedLetter(self.transitions[letterIndex], self.sumList[letterIndex]))
        return ''.join(word)

    def __main__(self):
        print("Generated word is %s" % self.genRandWord())
