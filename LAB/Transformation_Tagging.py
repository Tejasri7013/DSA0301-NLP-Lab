# Baseline step: Assign all words a default tag (e.g., NN for Noun)
tokens = [("The", "NN"), ("cat", "NN"), ("sat", "NN")]

print("Baseline Tags:")
print(tokens)

# Transformation Rule: Change tag from 'NN' to 'DT' (Determiner) if the word is 'The'
transformed_tokens = []
for word, tag in tokens:
    if word.lower() == "the" and tag == "NN":
        new_tag = "DT"
    else:
        new_tag = tag
    transformed_tokens.append((word, new_tag))

print("\nAfter Applying Transformation Rule:")
print(transformed_tokens)