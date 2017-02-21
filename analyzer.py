import pickle
import twitter
import random

markov = dict()

def remove_stuff(statuses):
    '''
    Remove the urls and hashtags that sometimes appear at the end of the
    status messages
    Returns a list of status texts
    '''
    res = []
    for status in statuses:
        cur = status.text
        while cur.find('https:')>0:
            cur = cur[:cur.find('https:')]
        res.append(cur)
    return res

def generate_markov(messages,num=2):
    '''
    Process the input message and generate a markov map for the prefix and surfix.
    '''
    global markov
    for i in range(len(messages)):
        message = messages[i]
        current_words = tuple()
        for word in message.rstrip().split():
            word = word.strip('@')
            word = word.strip('#')
            word = word.lower()
            if len(current_words)<num:
                current_words= current_words + (word,)
            else:
                if markov.get(current_words,0) == 0:
                    markov[current_words] = [word]
                else:
                    markov[current_words].append(word)
                current_words = current_words[1:]+ (word,)

def generate_random():
    '''
    Generate a random tweet based on the markov maping.
    '''
    global markov
    #current_words = random.choice(list(markov.keys()))
    current_words = ('i','think')
    tweet = current_words[0] + ' '+ current_words[1]
    while markov.get(current_words,0)!= 0:
        random_word = random.choice(markov[current_words])
        tweet = tweet + ' ' + random_word
        current_words = current_words[1:]+ (random_word,)
    return tweet

d = open('data.txt','rb')
statuses = pickle.load(d)
d.close
messages = remove_stuff(statuses)
generate_markov(messages)
num_times = 5
for i in range(num_times):
    tweet = generate_random()
    print(tweet)
