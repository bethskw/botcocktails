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
p = re.compile('make me an? ([^,\.@\?]+)', re.I)
p2 = re.compile('make a ([^,\.@\?]+)', re.I)
p3 = re.compile('make \w* ?a ([^,\.@\?]+)', re.I)


# read mentions
mentions=api.mentions_timeline(count=200) 
for mention in mentions:
    if mention.favorited:
        continue
    mymatch = p.search(mention.text)
    if (mymatch):
        cocktailname = mymatch.group(1) + ' - ' 
        print("Ooh a customer!")
        print ("I'm going to make a " + cocktailname)

        # ask for stuff from trained neural net
        t = textgenrnn('/home/beth/cocktails/textgenrnn_weights.hdf5')
        recipes = t.generate(1, temperature=1.0, prefix=cocktailname, return_as_list=True)
        tweet = recipes[0]

        # shorten if necessary
        if len(tweet) > 256:
            tweet = tweet[0:255]

        
        print(dir(mention.user))
        #api.update_status(tweet) 
        tweetid = str(mention.id)

        tweet = '@' + mention.user.screen_name + ' Here is your ' + tweet

        print(tweet + " (replying to " + tweetid + ")")
        api.update_status(tweet, in_reply_to_status_id=mention.id)
        mention.favorite() # fave to remember that we've seen it
