from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('tech-events.txt', num_epochs=20)

textgen.generate()
