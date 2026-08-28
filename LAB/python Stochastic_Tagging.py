import nltk
from nltk.tag import UnigramTagger

# Download the treebank corpus for training data
nltk.download('treebank')

# Load sample tagged sentences to act as our training data
train_sents = nltk.corpus.treebank.tagged_sents()[:100]

# Train the stochastic tagger based on word frequencies in the training data
uni_tagger = UnigramTagger(train_sents)

# Test the tagger on a new sentence
test_sentence = ["The", "dog", "ran"]
print("Stochastic Tagging Results:")
print(uni_tagger.tag(test_sentence))