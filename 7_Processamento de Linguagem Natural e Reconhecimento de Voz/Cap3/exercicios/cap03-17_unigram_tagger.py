# Unigram-Tagger

# Imports
import nltk
from nltk.corpus import mac_morpho

# Buscando os tokens etiquetados no corpus
tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
print("\nTokens etiquetados")
print(tagged_sents)

# Definindo nosso texto
texto = 'A manhã está ensolarada'

# Tokenização
tokens = nltk.word_tokenize(texto)

# Aplicando Unigram Tagger
unigram_tagger = nltk.tag.UnigramTagger(tagged_sents)

# Print
print("\nTexto etiquetado")
print(unigram_tagger.tag(tokens))
print("\n")

