import nltk
from nltk.stem import WordNetLemmatizer

# Download the required dictionary file for lemmatization
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
print("Verb Lemma:", lemmatizer.lemmatize("running", 'v'))
print("Noun Lemma:", lemmatizer.lemmatize("cats", 'n'))