import nltk

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> 'John'
  VP -> 'runs'
""")

parser = nltk.ChartParser(grammar)
print("Generated Graphical Parse Tree:")
for tree in parser.parse(['John', 'runs']):
    tree.pretty_print()