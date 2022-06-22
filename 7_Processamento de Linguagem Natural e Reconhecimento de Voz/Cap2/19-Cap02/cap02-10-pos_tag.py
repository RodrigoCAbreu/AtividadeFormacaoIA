# Part-of-Speech Tagging

# O POS Tagging é o processo de rotulação de elementos textuais - tipicamente palavras e pontuação - com o fim de evidenciar 
# a estrutura gramatical de um determinado trecho de texto. 
# Em reconhecimento e síntese de fala, seu uso é útil para extração de termos, desambiguação, composição de novas frases e pesquisa lexicográfica.

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

# Texto
frase = "Time to start with natural language processing. Python will make our life easier!"

# Tokenization em sentenças
sent_tokens = sent_tokenize(frase)
print(sent_tokens)

# Tokenization em palavras
word_tokens = word_tokenize(frase)
print(word_tokens)

# Aplicando pos_tag aos tokens
tags = pos_tag(word_tokens)

# Print na tela
print(tags)

# Visualizando o significado de cada código do POS Tag.
# Nesse caso, visualizando VB
nltk.help.upenn_tagset('VB')

# Definição para cada definição de código
list_of_tags = []
for pair in tags:
    list_of_tags.append(pair[1])
list_of_tags = list(set(list_of_tags))
list_of_tags


for pos in list_of_tags:
    print(nltk.help.upenn_tagset(pos))