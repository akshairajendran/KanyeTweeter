__author__ = 'arajendran'

from lxml import html
import cPickle as pickle
import requests
from unidecode import unidecode

#load website file
f = open('websites.txt','r')
websites = [site.strip() for site in f]

print websites

page = requests.get(websites[0])
tree = html.fromstring(page.text)

tweets = tree.xpath('//p[@class="text"]/text()')
tweets_encode = [unidecode(tweet) for tweet in tweets]

hashtags = tree.xpath('//a[@class="hashtag"]/text()')
hashtags_encode = [unidecode(hashtag) for hashtag in hashtags]

print tweets_encode
print hashtags_encode


