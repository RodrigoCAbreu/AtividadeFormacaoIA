# Default Tagger

# Imports
import nltk
from nltk.corpus import mac_morpho

# Buscando os tokens etiquetados no corpus
sentencas_etiquetadas = mac_morpho.tagged_sents()
print("\nSentenças etiquetados")
print(sentencas_etiquetadas)

# Definindo nosso texto
texto = 'A manhã está ensolarada'

# Tokenização
tokens = nltk.word_tokenize(texto)

# Aplicando Tagger
tags = [tag for (word, tag) in mac_morpho.tagged_words()]
nltk.FreqDist(tags).max()

# Definindo uma tag padrão a todas as palavras
etiqPadrao = nltk.tag.DefaultTagger('N')

# Print
print("\nTexto etiquetado")
print(etiqPadrao.tag(tokens))
print("\n")

