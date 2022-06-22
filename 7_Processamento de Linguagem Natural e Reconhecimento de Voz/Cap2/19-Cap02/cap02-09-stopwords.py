# Remoção de Stopwords

# Stopwords são palavras comuns que normalmente não contribuem para o significado de uma frase, pelo menos com relação ao propósito da 
# informação e do processamento da linguagem natural. São palavras como "The" e "a" ((em inglês) ou "O/A" e "Um/Uma" ((em português). 
# Muitos mecanismos de busca filtram estas palavras (stopwords), como forma de economizar espaço em seus índices de pesquisa.

# Imports
from nltk.corpus import stopwords

# Stop words em inglês
english_stops = set(stopwords.words('english'))

# Lista de palavras
words = ["Can't", 'is', 'a', 'contraction']

# List comprehension para aplicar as english_stop words a lista de palavras
[word for word in words if word not in english_stops]

#Stop words em português
portuguese_stops = set(stopwords.words('portuguese'))

# Lista de palavras
palavras = ["Estou", 'estudando', 'um', 'tema', 'interesante', 'em', 'PLN']

# List comprehension para aplicar as portuguese_stop words a lista de palavras
[palavra for palavra in palavras if palavra not in portuguese_stops]

# IDs das Stop Words
stopwords.fileids()

# Stop words
stopwords.words('portuguese')