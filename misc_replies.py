import random
from textgenrnn import textgenrnn
import tweepy
from secrets import *

# twitter auth
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)


# going to try a regular expression here
import re
react_ew = re.compile('\\bew+?\\b', re.I)

# read mentions
mentions=api.mentions_timeline(count=200) 
for mention in mentions:
    if mention.favorited:
        continue
    mymatch = react_ew.search(mention.text)
    if (mymatch):
        tweet = 'SORRY'

        # shorten if necessary
        if len(tweet) > 256:
            tweet = tweet[0:255]

        
        print(dir(mention.user))
        #api.update_status(tweet) 
        tweetid = str(mention.id)

        tweet = '@' + mention.user.screen_name + ' ' + tweet

        print(tweet + " (replying to " + tweetid + ")")
        api.update_status(tweet, in_reply_to_status_id=mention.id)
        mention.favorite() # fave to remember that we've seen it


