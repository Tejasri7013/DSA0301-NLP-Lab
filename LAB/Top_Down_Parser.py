import nltk

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'the'
  N -> 'cat'
  V -> 'chased'
""")

parser = nltk.RecursiveDescentParser(grammar)
sentence = ['the', 'cat', 'chased', 'the', 'cat']
print("Top-Down Parsing Trees:")
for tree in parser.parse(sentence):
    print(tree)