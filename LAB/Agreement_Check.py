import nltk
# Import FeatureGrammar from the specific sub-module
from nltk.grammar import FeatureGrammar

grammar = FeatureGrammar.fromstring("""
  S -> NP[NUM=?n] VP[NUM=?n]
  NP[NUM=?n] -> N[NUM=?n]
  VP[NUM=?n] -> V[NUM=?n]
  N[NUM=sing] -> 'dog'
  V[NUM=sing] -> 'barks'
""")

parser = nltk.FeatureChartParser(grammar)
print("Checking Agreement for 'dog barks':")
for tree in parser.parse(['dog', 'barks']):
    print(tree)