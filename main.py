#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random
from MarkovGenerator import MarkovGenerator
from textblob import TextBlob
from pprint import pprint
 
# Authorizations.
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_KEY = 'your_access'
ACCESS_SECRET = 'your_secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
textFile = open('path/to/text/file')

mark = MarkovGenerator(textFile, 2)

opening = ['Can you imagine this? ', 'Can you imagine that? ', 'Wow... right? ',
			'Right!?! ', 'Man... ', 'Guy!! ', 'Come on... man... ', 'WOW ']

time.sleep(60 * 5)

while True:
	if (random.randint(0, 100) < 40):
		tweet = opening[random.randint(0, len(opening) - 1)] + mark.generateText(20)
	else:
		tweet = mark.generateText(20)
	print(tweet[0:139])
	api.update_status(tweet[0:139])
	time.sleep(3600)
	
