# Basic tokenization mapping for logical expressions using Python's built-in tools
expr = "forall x (Cat(x) -> Animal(x))"
tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
print("Logical Proposition Expression Tokens:")
print(tokens)