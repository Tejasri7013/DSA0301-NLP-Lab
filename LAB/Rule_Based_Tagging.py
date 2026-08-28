import nltk
from nltk.tag import RegexpTagger

# Define morphological patterns and their matching POS tags
patterns = [
    (r'.*ing$', 'VBG'),   # Gerunds / present participles (e.g., running)
    (r'.*ed$', 'VBD'),    # Past tense verbs (e.g., jumped)
    (r'.*s$', 'NNS'),     # Plural nouns (e.g., cats)
    (r'.*', 'NN')         # Default fallback: Singular noun
]

tagger = RegexpTagger(patterns)
words = ["running", "cats", "jumped", "dog"]

print("Rule-Based Tagging Results:")
print(tagger.tag(words))