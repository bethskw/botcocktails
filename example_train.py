###
# This script trains a neural network. 
# You need: 
# 1. A list of things (eg cocktail recipes) one per line
# 2. textgenrnn, which requires TensorFlow
# 3. Some time. Training takes a while. Read up on this, okay?
# This might help (includes sample code) https://lifehacker.com/we-trained-an-ai-to-generate-lifehacker-headlines-1826616918

from textgenrnn import textgenrnn

t = textgenrnn();
# on subsequent runs, replace the above line with this one to load the file this creates: t = textgenrnn('textgenrnn_weights.hdf5')

t.train_from_file('input.txt', num_epochs=10)
# you might want more than 10 epochs, of course.


