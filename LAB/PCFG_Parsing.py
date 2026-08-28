import nltk
# Import PCFG from the correct grammar sub-module
from nltk.grammar import PCFG

pcfg = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> 'John' [1.0]
  VP -> 'runs' [1.0]
""")

parser = nltk.ViterbiParser(pcfg)
print("Probabilistic Parsing Tree (Viterbi):")
for tree in parser.parse(['John', 'runs']):
    print(tree)