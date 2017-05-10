import data_finder
from pickle import dump, load
import random

class Auto_Tweeter:
    def __init__ (self):
        self.data_grab()
        self.tweet_maker()

    def data_grab(self):
        # asks if you need to pull new data for this person
        print ('What is the handle of the person you want to mimic?')
        self.user_handle = input()

        print ('Have you collected Data? (y/n)')
        collect_data = input()
        #pulls new data, by calling Auto_tweeter
        if collect_data == 'n':
            self.statuses = data_finder.data_finder(self.user_handle)
            self.dictionary_maker() # calls the dictionary_maker method
    def dictionary_maker(self):
        #sorts data into for markov analysis
        self.dictionary = {}
        self.start = []
        self.end = []
        for tweet in self.statuses:
            # collects all the starts of each tweet
            self.each_start = [[tweet[0],tweet[1]]]
            self.start = self.start + self.each_start
        self.dictionary['START']= self.start
        for tweet in self.statuses:
            tweet += ['END'] # adding and end flag to the end of the tweet
            i= len(tweet)
            for x in range (0,(i-2)):
                #forming a dictionary linking previos two to the next word
                if tweet[x]+tweet[x+1] in self.dictionary:
                    self.dictionary[tweet[x]+tweet[x+1]] += [tweet[x+2]]
                else:
                    self.dictionary[tweet[x]+tweet[x+1]] = [tweet[x+2]]

        self.pickle()

    def pickle(self):
        #saves the data set in a file
        Data_Set = open(str(self.user_handle)+'.txt','wb')
        dump(self.dictionary, Data_Set)
        Data_Set.close()


    def tweet_maker(self):
        Data_Set = open(str(self.user_handle)+'.txt','rb')
        #loading the data
        self.dictionary = load(Data_Set)
        print(len(self.dictionary['START']))
        self.new_tweet=[]
        self.new_tweet += random.choice(self.dictionary['START'])
        #starts the tweet off with a random begining
        #keeps adding randomly untill we arive at an END
        while not self.new_tweet[-1] == 'END':
            self.new_tweet += [random.choice(self.dictionary[self.new_tweet[-2]+self.new_tweet[-1]])]
        self.final_tweet = ' '
        #adds the words together and adds spaces
        for word in self.new_tweet:
            if not word =='END':
                self.final_tweet += ' ' + word
        #prints the new tweet
        print(str(self.user_handle)+' says:'+ self.final_tweet)

        print('Make another tweet (y/n)')
        another= input()
        if another == 'y':
            self.tweet_maker()

if __name__ == '__main__':
    tweeter = Auto_Tweeter()
