# Aplicando TF-IDF em um conjunto de dados
# http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

# Imports
import os
import nltk
import string
import numpy as np
from nltk.stem.porter import *
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Função para obter os tokens
def get_tokens():
   with open('shakes/shakes1.txt', 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()

    # Remove a pontuação usando a etapa de exclusão de caracteres da função translate()
    no_punctuation = lowers.translate(string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

# Obtém os tokens
tokens = get_tokens()
print("\nTokens: ", tokens)

# Remove as Stop words
filtered = [w for w in tokens if not w in stopwords.words('english')]
print("\nTokens sem stop words: ", tokens)

# Função para Stem
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

# Aplica o Stem
stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
print("\nTokens sem stop words e com stemming: ", stemmed)

# Variáveis de automatização
path = 'shakes'
token_dict = {}

# Tokenização
def tokenize(text):
    no_punctuation = lowers.translate(string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    stems = stem_tokens(tokens, stemmer)
    return stems

# Obtém todos os arquivos no Corpus e remove a pontuação
for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(string.punctuation)
        token_dict[file] = no_punctuation

# Calcula o TF-IDF
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

print("\nFeatures")
feature_names = tfidf.get_feature_names()
for col in tfs.nonzero()[1]:
    print (feature_names[col], ' - ', tfs[0, col])


