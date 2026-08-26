from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "The sky is blue.", 
    "The sun is bright.", 
    "The sun and the sky."
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(docs).toarray()

print("TF-IDF Vector Space Matrix:")
print(matrix)
print("\nVocabulary words mapping:")
print(vectorizer.get_feature_names_out())