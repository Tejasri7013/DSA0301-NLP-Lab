import nltk
from nltk.wsd import lesk

# Ensure WordNet is available
nltk.download('wordnet')
nltk.download('punkt')

sentence = nltk.word_tokenize("I went to the bank to deposit cash.")
sense = lesk(sentence, 'bank')

print("Contextually Disambiguated Sense:")
if sense:
    print(f"Sense: {sense.name()} | Definition: {sense.definition()}")
else:
    print("No match found.")