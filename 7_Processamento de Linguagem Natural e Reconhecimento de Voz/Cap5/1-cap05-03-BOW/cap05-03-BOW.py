# BOW

# Execute: python cap05-03-BOW.py

# Imports
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Cria um ngram vectorizer
# Vamos criar o BOW de 2 documentos, que neste caso serão as palavras: words e wprds
# Usamos n_gram = 2 no nível de unidade de caracter
ngram_vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2), min_df=1)

# Contabilizamos as combinações de caracteres nas palavras
counts = ngram_vectorizer.fit_transform(['words', 'wprds'])
ngram_vectorizer.get_feature_names() == (['w', 'ds', 'or', 'pr', 'rd', 's ', 'wo', 'wp'])

# Imprimimos o BOW
print (counts.toarray().astype(int))
