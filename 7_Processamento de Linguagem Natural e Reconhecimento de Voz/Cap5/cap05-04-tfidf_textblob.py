# TF-IDF com Textblob

# pip install textblob

# Imports
from textblob import TextBlob
import math

# TF
def tf(word, blob):
       return blob.words.count(word) / len(blob.words)

# Verifica palavra mno texto
def n_containing(word, bloblist):
    return 1 + sum(1 for blob in bloblist if word in blob)

# IDF
def idf(word, bloblist):
    x = n_containing(word, bloblist)
    return math.log(len(bloblist) / (x if x else 1))

# Score TF-IDF
def tfidf(word, blob, bloblist):
   return tf(word, blob) * idf(word, bloblist)

# Texto
text = 'tf idf, forma abreviada de frequência de termo, frequência de documento inversa'
text2 = 'é uma estatística numérica que se destina a refletir o quão importante'
text3 = 'uma palavra é para um documento em uma coleção ou corpus'

blob = TextBlob(text)
blob2 = TextBlob(text2)
blob3 = TextBlob(text3)
bloblist = [blob, blob2, blob3]

# Scores para a palavra: abreviada
tf_score = tf('abreviada', blob)
idf_score = idf('abreviada', bloblist)
tfidf_score = tfidf('abreviada', blob, bloblist)

# Print
print ("\n")
print ("TF Score para a palavra: abreviada     --- " + str(tf_score)+"\n")
print ("IDF Score para a palavra: abreviada    --- " + str(idf_score)+"\n")
print ("TF-IDF Score para a palavra: abreviada --- " + str(tfidf_score))
print ("\n")

