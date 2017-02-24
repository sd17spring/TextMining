import numpy as np
import random

class WordCreator(object):
    def __init__(self, filename=None, words=None):
        """
        Initializes variables in WordCreator object
        Creates Transition matrix and normalizes it
        Takes string path (filename), or string (words)
        """

        #Check whether input was text file or list of words
        if filename:
            self.txtFile = open(filename, 'r')
            self.words = None
        else:
            self.txtFile = None
            self.words = words

        #Initialize attributes
        self.transitions = np.zeros([256, 256])
        self.sumList = []
        self.minLetters = self.getMinLetters()
        self.maxLetters = self.getMaxLetters()

        #Run through training set and assign probabilities
        self.setTransitions()

    def getMaxLetters(self):
        """
        Returns the max number of letters in a word in the text file
        """

        currentMax = 0

        #If reading from text file
        if self.txtFile:
            self.txtFile.seek(0) #Go to beginning of file
            #Loop through file
            for word in self.txtFile:
                #Find longest word
                if len(word) >= currentMax:
                    currentMax = len(word)
        else:
            currentMax = 15
        #Else read from word list
        # else:
        #     #Loop through list
        #     for word in self.words:
        #         #Find longest word
        #         if len(word) >= currentMax:
        #             currentMax = len(word)
        # #Return length of longest word
        return currentMax

    def getMinLetters(self):
        """
        Returns the minimum number of letters in a word in the text file
        """

        currentMin = 10000  #Arbitrarily large starting minimum
        #If using text file
        if self.txtFile:
            #Go to beginning of text file
            self.txtFile.seek(0)
            #Loop through file
            for word in self.txtFile:
                #Find biggest word
                if len(word) <= currentMin:
                    currentMin = len(word)
        #Else use word list
        # else:
        #     #Loop through word list
        #     for word in self.words:
        #         #Find shortest word
        #         if len(word) <= currentMin:
        #             currentMin = len(word)
        #return shortest word length
        else:
            currentMin = 3

        return currentMin

    def setTransitions(self):
        """
        Sets the transitions attribute
        Loops through the text file and finds probabilities that
        letters transition into other letters
        Index m, n represents the probability that m transitions to n
        Index 27 represents a space input
        """
        #If using text file
        if self.txtFile:
            #Go to beginning of file
            self.txtFile.seek(0)
            #Loop through words
            for line in self.txtFile:
                line = line.lower()
                #Increment transition matrix ith letter, i+1th letter by 1
                for i in range(len(line)-1):
                    xInd = ord(line[i])
                    yInd = ord(line[i+1])
                    if not(xInd > 255 or yInd > 255):
                        self.transitions[xInd][yInd] += 1
        #Else use word list
        if self.words:
            #Loop through words
            for i in range(len(self.words)-1):
                #Increment transition matrix ith letter, i+1th letter by 1
                xInd = ord(self.words[i])
                yInd = ord(self.words[i+1])
                if not(xInd > 255 or yInd > 255):
                    self.transitions[xInd][yInd] += 1
        #Normalize Matrix and get totals of each character
        self.normalizeTransitions()

    def normalizeTransitions(self):
        """
        Adds up a row of transitions and divides it by the sum
        Adds sum to the list of sums (sumList)
        """
        #Reinitialize list of character appearances
        self.sumList = []

        #Loop through each row of Transition Matrix
        for i in range(len(self.transitions)):
            #Normalize row and add sum to the list of character appearances
            self.transitions[i], summation = self.norm(self.transitions[i])
            self.sumList.append(summation)

    def norm(self, lst):
        """
        Receives a list (lst) argument
        Normalizes the list
        Returns normalized list and sum of the original entities
        """
        #Initialize current sum and make copy of the input list
        summation = 0
        tempList = self.copyList(lst)

        summation = self.getSum(lst)

        #Loop through list again, dividing each entry by the sum of all entries
        for i in range(len(tempList)):
            tempList[i] = tempList[i]/summation

        #Return normalized list, and the sum of the original values
        return tempList, summation

    def getSum(self, lst):
        """
        Receives list of numbers
        Returns sum of the list
        """
        #Initialize sum
        summation = 0
        #Loop through list, adding up values
        for i in lst:
            summation += i

        #Return final sum
        return summation

    def copyList(self, lst):
        """
        Receives list (lst)
        Returns copy of list (copy)
        Exists so attributes don't get changed in methods unless
        otherwise specified
        """

        #Initialize copy
        copy = []

        #Add all elements of lst to copy
        for i in lst:
            copy.append(i)

        #return copy
        return copy


    def getRanges(self, probList, summation):
        """
        Turns list of probabilities of transition into ranges
        for random numbers.
        Receives probability list (probList) and
        sum of original values (summation)
        Returns list of selection ranges (ranges) and their indexes
        in the original list (indices)
        """
        #Initialize method variables
        lastVal = 0
        tempList = self.copyList(probList)
        ranges = []
        indices = []

        #Loop through list of probabilities
        for i in range(len(tempList)):
            #If the current index is non-zero
            if tempList[i]:
                #Un-Normalize the value
                tempList[i] = tempList[i] * summation

                #Add the running sum to it
                ranges.append(lastVal + tempList[i])

                #Append it to the return list
                indices.append(i)

                #Add the value to un-normed value to the running sum
                lastVal += tempList[i]

        #Return the list of ranges and the original indices of the ranges
        return ranges, indices


    def getWeightedLetter(self, probList, inSum):
        """
        Receives list of probabilities (probList) and sum of original entities
        of the list
        Generates random letter based on how the letter is weighted in the list
        returns that number
        """
        print(inSum)
        #Get probability ranges and their indices
        ranges, indices = self.getRanges(probList, inSum)
        randLetterIndex = random.randint(1, inSum)
        lastVal = 0
        #Loop through values in ranges
        for i in range(len(ranges)):
            #If random integer is between the previous and current range
            if lastVal < randLetterIndex and randLetterIndex <= ranges[i]:
                #return the character at that index
                return chr(indices[i])
            #Reinitialize last value
            lastVal = ranges[i]


    def genWord(self, n):
        """
        Generates random word based on transition list of length n
        Returns a word (word)
        """
        #Initiealize method variables
        word = []
        wordLen = n

        #Create normalized list of sums and get the total characters
        normList, totalChar = self.norm(self.sumList)

        #Get a letter based on the frequency of letters in the set
        word.append(self.getWeightedLetter(normList, totalChar))

        #loop until you hit the end of the word length
        for i in range(wordLen-1):
            #append random character based on the previous character
            letterIndex = ord(word[i])
            flag = True
            subtractor = 1
            while flag:
                if self.sumList[letterIndex]:
                    word.append(self.getWeightedLetter(self.transitions[letterIndex], self.sumList[letterIndex]))
                    flag = False
                else:
                    letterIndex  = ord(word[i-subtractor])
                    subtractor+=1



        #return word as a string
        return ''.join(word)

    def genRandWord(self):
        """
        Generates random word based on transition list
        Returns a word (word)
        Same as genWord(), but with a random word length
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
        """
        Main function. Generates random word
        """

        print("Generated phrase is %s" % self.genRandWord())
