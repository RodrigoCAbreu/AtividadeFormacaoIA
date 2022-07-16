# Classificação Naive Bayes - v2

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

# Lista de todas as palavras
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Calculando a frequência das palavras
all_words = nltk.FreqDist(all_words)

# Objeto para a lista de features das 3.000 palavras mais frequentes
word_features = list(all_words.keys())[:3000]

# Buscando as features
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# Buscando as features em um dos arquivos do dataset
print("\nBuscando as features em um dos arquivos do dataset: ")
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# Criando o conjunto de features para todos os documentos
featuresets = [(find_features(rev), category) for (rev, category) in documents]

