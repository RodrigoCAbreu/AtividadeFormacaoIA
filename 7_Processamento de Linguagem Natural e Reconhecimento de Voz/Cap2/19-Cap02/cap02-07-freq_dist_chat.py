# Explorando Distribuição de Frequência em Dados de Chat

# Imports
import nltk
from nltk.corpus import webtext

# Fileids
print("\n")
print(webtext.fileids())

# Distribuição de frequência de um único arquivo
fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)

# Report
print('\nContagem do número máximo de ocorrências do token "',fdist.max(),'" : ', fdist[fdist.max()])
print('\nNúmero total de tokens distintos : ', fdist.N())
print('\nA seguir estão os 10 tokens mais comuns')
print(fdist.most_common(10))
print("\n")