# Extraindo a Distribuição de Frequência de Palavras de um Corpus

# Imports
import nltk
from nltk.corpus import brown

# Imprimindo as categorias
print("\nCategorias no Corpus:")
print(brown.categories())

# Lista com algumas das categorias
genres = ['fiction', 'humor', 'romance']

# Palavras começando com o sufixo wh
whwords = ['what', 'which', 'why', 'when', 'where', 'who']

# Calculando a Distribuição de Frequência com a função FreqDist()
for i in range(0,len(genres)):
    genre = genres[i]
    print()
    print("\nAnalisando '"+ genre + "' e extraindo palavras com sufixo wh")
    genre_text = brown.words(categories = genre)
    fdist = nltk.FreqDist(genre_text)
    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')

print("\n")