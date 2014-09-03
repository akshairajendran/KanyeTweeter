__author__ = 'Akshai Rajendran'

import cPickle as pickle
import random

#create Markov class
class Markov(object):
    #take in a list of tweets and the n for ngram
    #split the tweets into individual words
    #create the blank dictionary cache
    #run the database function to populate cache
    def __init__(self,list,n):
        self.list = list
        self.n = n
        self.split_list = self.list_split()
        self.cache = {}
        self.database()
    #split up a list of tweets into a list of lists of individual words
    def list_split(self):
        split = [string.split() for string in self.list]
        return split
    #return ngrams for a given string and n
    def ngram(self,string):
        if len(string) < self.n:
            return
        for i in range(len(string) - self.n + 1):
            yield [string[i+index] for index in range(self.n)]
    #this function populates the cache
    #it takes the list of tweets and uses the ngram function to create the dictionary
    def database(self):
        for string in self.split_list:
            for set in self.ngram(string):
                key = set[:-1]
                if tuple(key) in self.cache:
                    self.cache[tuple(key)].append(set[-1])
                else:
                    self.cache[tuple(key)] = [set[-1]]
    #generate a tweet of a given length using the dictionary
    def gen_tweet(self, size=15):
        seed_key = random.randint(0,len(self.cache.keys())-1)
        seed = self.cache.keys()[seed_key]
        tweet = list(seed)
        i = len(tweet)
        while i <= size:
            if seed in self.cache.keys():
                rand_word = random.choice(self.cache[seed])
                tweet.append(rand_word)
            else:
                return ' '.join(tweet)
            temp = list(seed)
            temp.pop(0)
            temp.append(rand_word)
            seed = tuple(temp)
            i+=1
        return ' '.join(tweet)

def tweet(start=5,end=15,n=2):
    #load pickle dbs into lists
    tweets = pickle.load(open('ye_tweets.p','rb'))
    hashtags = pickle.load(open('ye_hashtags.p','rb'))

    #create Markov class
    markov = Markov(tweets,n)

    #generate tweet of random length between start and end
    tweet_result = markov.gen_tweet(random.randint(start,end))

    #strip out trailing ',",/
    tweet_result = tweet_result.replace('"','')
    tweet_result = tweet_result.replace('/','')
    tweet_result = tweet_result.replace("'",'')
    tweet_result = tweet_result.replace("(",'')
    tweet_result = tweet_result.replace(")",'')

    #1 out of 5 times append a hashtag
    if random.randint(1,5) == 1:
        return tweet_result + " " + random.choice(hashtags)
    else:
        return tweet_result






