import nltk

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'the'
  N -> 'cat'
  V -> 'chased'
""")

parser = nltk.EarleyChartParser(grammar)
sentence = ['the', 'cat', 'chased', 'the', 'cat']
print("Earley Parsing Trees:")
for tree in parser.parse(sentence):
    print(tree)