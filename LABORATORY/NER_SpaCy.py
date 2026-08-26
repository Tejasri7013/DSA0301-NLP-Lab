import nltk

# Download required datasets for NLTK NER chunking
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "Apple is looking at buying U.K. startup for $1 billion"

# Tokenize and tag parts of speech
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

# Extract named entities
chunks = nltk.ne_chunk(pos_tags)

print("Named Entities Found:")
for chunk in chunks:
    if hasattr(chunk, 'label'):
        entity_name = " ".join([c[0] for c in chunk])
        print(f"Entity: {entity_name} | Label: {chunk.label()}")