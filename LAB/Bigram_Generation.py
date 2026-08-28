import random

text = "cat sat on the mat cat sat on the rug"
tokens = text.split()

# Create bigrams: pairs of consecutive words
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]

# Build the bigram model dictionary
model = {}
for w1, w2 in bigrams:
    model.setdefault(w1, []).append(w2)

# Generate text starting with the word "cat"
current = "cat"
gen = [current]
for _ in range(5):
    if current in model:
        current = random.choice(model[current])
        gen.append(current)
    else:
        break

print("Generated Text Sequence:")
print(" ".join(gen))