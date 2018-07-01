#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
import random
from time import sleep
from responses import *

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

num=0
count=0
temp=0

while (count < 4):

    firstTweet = api.search("Hillary")[0]
    if firstTweet.id==temp:
       sleep(15)
       continue

    rid=firstTweet.id
    rsn=firstTweet.user.screen_name

    m="@%s "% (rsn) + random.choice(response)
    api.update_status(status=m, in_reply_to_status_id=rid)

    count=count+1
    print(count)
    print(m)
    temp = firstTweet.id
