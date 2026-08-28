import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The tall cat chased a mouse."
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

# Define a grammar pattern to extract Noun Phrases (NP)
# An NP is an optional determiner (DT), followed by zero or more adjectives (JJ), and a noun (NN)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(pos_tags)

print("Extracted Noun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join([word for word, tag in subtree.leaves()])
        print(f"- Noun Phrase: '{phrase}'")