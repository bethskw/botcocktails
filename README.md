# botcocktails

# What this bot does #

This is a twitter bot that tweets recipes (or whatever you want) from a
trained neural network.

# How to set up the neural network #

1. Make sure you have the textgenrnn module (which itself requires
TensorFlow).

2. Collect a list of things, one per line. This code comes with a file
called input.txt, which contains cocktail recipes from Wikipedia.

3. Use the included example_train.py to train a neural network from the
input file. (See the textgenrnn docs for more information.) 

4. This creates a file called textgenrnn_weights.hdf5. In this distribution
you'll find an example file of this name. it's been very lightly trained and
is probably no fun, but it's enough to let you test the code. 

# How to set up the twitter bot #

1. Create a twitter account for your bot. 

2. Copy the API keys and secrets into the file here called secrets.py.

3. Set up a cron job to run bot.py on whatever interval you like. 

4. For replies to work, set up a cron job to run the other files once per
minute (or at the interval of your choice). The bot will 'like' each request
it replies to, so that it knows not to reply to the same one again. 

# What if this breaks? #

It probably will. You get to keep both pieces.

