# Usando N-grams com NLTK

# Imports
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

# Texto
text = "Eu preciso escrever um programa em NLTK que quebra um corpus (uma grande coleção de arquivos txt) em unigrams, bigrams, trigramas, quatro gramas e cinco gramas. Eu preciso escrever um programa em NLTK que quebra um corpus"

# Tokenização
token = nltk.word_tokenize(text)

# N-gramas
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)

# Print
print("\nTexto Original: ")
print(text)
print("\nBigramas: ")
print (Counter(bigrams))
print("\n")


