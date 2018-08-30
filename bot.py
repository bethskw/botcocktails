import random
from textgenrnn import textgenrnn
import tweepy
from secrets import *

# twitter auth
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

# get random words
word_file = "/home/beth/cocktails/words.txt"
words = open(word_file).read().splitlines()

w1 = words[random.randint(1,len(words)-1)].capitalize()
w2 = words[random.randint(1,len(words)-1)].capitalize()

cocktailname = w1 + ' ' + w2  + ' - '
print ("I'm going to make a " + cocktailname)

# ask for stuff from trained neural net
t = textgenrnn('/home/beth/cocktails/textgenrnn_weights.hdf5')
recipes = t.generate(1, temperature=1.0, prefix=cocktailname, return_as_list=True)

# tweet!
tweet = recipes[0]

if len(tweet) > 256:
    tweet = tweet[0:255]


api.update_status(tweet) 
print(tweet)
