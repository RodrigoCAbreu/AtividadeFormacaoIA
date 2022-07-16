# Classificação Naive Bayes - v1

# Imports
import nltk
import random
from nltk.corpus import movie_reviews

# Documentos
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle
random.shuffle(documents)

# Print de um dos documentos
print("\nImprimindo um dos documentos: ")
print(documents[1])

# Lista de todas as palavras
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Calculando a frequência das palavras
all_words = nltk.FreqDist(all_words)

# Imprimindo as mais comuns
print("\nImprimindo as 15 palavras mais comuns: ")
print(all_words.most_common(15))

# Imprimindo quantas vezes uma palavra específica aparece
print("\nImprimindo o número de ocorrências da palavra store: ")
print(all_words["store"])
