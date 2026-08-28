import nltk
from nltk.corpus import wordnet

# Download the wordnet dictionary
nltk.download('wordnet')

syns = wordnet.synsets("bank")
print("Synset Definitions for 'bank':")
for syn in syns[:3]:
    print(f"- {syn.name()}: {syn.definition()}")