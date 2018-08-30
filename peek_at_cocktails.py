from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5')
textgen.generate(20, temperature=0.5)
