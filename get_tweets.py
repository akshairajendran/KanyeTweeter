__author__ = 'arajendran'

from lxml import html
import cPickle as pickle
import requests
from unidecode import unidecode

#load website file
f = open('websites.txt','r')
websites = [site.strip() for site in f]

#for each site, create a page
pages = [requests.get(site) for site in websites]

#for each page create a tree
trees = [html.fromstring(page.text) for page in pages]

#for each tree create a list of all tweets from that month, then flatten
#then unicode
tweets = [tree.xpath('//p[@class="text"]/text()') for tree in trees]
tweets = [tweet for sublist in tweets for tweet in sublist]
tweets_encode = [unidecode(tweet) for tweet in tweets]

#for each tree create a list of all hashtags from that month,  then flatten
#then unicode
hashtags = [tree.xpath('//a[@class="hashtag"]/text()') for tree in trees]
hashtags = [hashtag for sublist in hashtags for hashtag in sublist]
hashtags_encode = [unidecode(hashtag) for hashtag in hashtags]

#dump both to pickle dbs
pickle.dump(tweets_encode, open('ye_tweets.p','wb'))
pickle.dump(hashtags_encode, open('ye_hashtags.p','wb'))


