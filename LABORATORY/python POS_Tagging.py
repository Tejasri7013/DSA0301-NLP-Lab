import nltk

# Download the required tokenization and tagging data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = nltk.word_tokenize("The quick brown fox jumps.")
print("POS Tags:")
print(nltk.pos_tag(text))