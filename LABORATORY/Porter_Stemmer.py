from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "runs", "runner", "easily"]

print("Stemming Results:")
for w in words:
    print(f"{w} -> {ps.stem(w)}")