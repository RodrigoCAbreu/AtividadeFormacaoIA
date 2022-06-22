# Stemming

# Stemming é a técnica de remover sufixos e prefixos de uma palavra, chamada stem. 
# Por exemplo, o stem da palavra cooking é cook. Um bom algoritmo sabe que "ing" é um sufixo e pode ser removido. 
# Stemming é muito usado em mecanismos de buscas para indexação de palavras. 
# Ao invés de armazenar todas as formas de uma palavras, um mecamismo de busca armazena apenas o stem da palavra, 
# reduzindo o tamanho do índice e aumentando a performance do processo de busca.

# Import
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

# Cria o Stemmer
stemmer = PorterStemmer()

# Aplica o Stemmer
print("\nPorterStemmer")
print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))

# Cria o Stemmer
stemmer2 = LancasterStemmer()

# Aplica o Stemmer
print("\nLancasterStemmer")
print(stemmer2.stem('cooking'))
print(stemmer2.stem('cookery'))

# Cria o Stemmer
stemmer3 = RegexpStemmer('ing')

# Aplica o Stemmer
print("\nRegexpStemmer")
print(stemmer3.stem('cooking'))
print(stemmer3.stem('cookery'))

# Cria o Stemmer
SnowballStemmer.languages
portuguese_stemmer = SnowballStemmer('portuguese')
print("\nSnowballStemmer")
print(portuguese_stemmer.stem('Tudo bem'))

