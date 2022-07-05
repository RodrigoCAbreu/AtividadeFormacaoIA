# Treinando Seu Próprio POS-Tagger
# NLTK pos_tag() - http://www.nltk.org/book/ch05.html

# Imports
import nltk
import pickle

# Amostra de dados
def sampleData():
    return [
        "New York is the capital of United States.",
        "Steve Jobs was the CEO of Apple.",
        "iPhone was Invented by Apple.",
        "Books can be purchased in Market.",
    ]

# Função para criar um dicionário
def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        partsOfSpeechTags = nltk.pos_tag(nltk.word_tokenize(sent))
        for tag in partsOfSpeechTags:
            value = tag[0]
            pos = tag[1]
            dictionary[value] = pos
    print("\nDicionário Criado:")
    print(dictionary)        
    return dictionary

# Função para salvar o Tagger
def saveMyTagger(tagger, fileName):
    fileHandle = open(fileName, "wb")
    pickle.dump(tagger, fileHandle)
    fileHandle.close()

# Função para salvar o treinamento
def Training(fileName):
    tagger = nltk.UnigramTagger(model=buildDictionary())
    saveMyTagger(tagger, fileName)

# Função para carregar o tagger
def loadMyTagger(fileName):
    return pickle.load(open(fileName, "rb"))

# Texto
sentence = 'iPhone is purchased by Steve Jobs in New York Market'

# Nome do Tagger
fileName = "myTagger.pickle"

# Treninamento
Training(fileName)

# Carregando o treinamento
myTagger = loadMyTagger(fileName)

# Print
print("\nImprimindo o resultado após o POS Tagger")
print(myTagger.tag(nltk.word_tokenize(sentence)))
print("\n")
