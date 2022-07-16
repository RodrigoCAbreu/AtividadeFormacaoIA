# Classificação Naive Bayes - v3

# Imports
import nltk
import random
import pickle
from nltk.corpus import movie_reviews

# Documentos
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle
random.shuffle(documents)

# Lista de todas as palavras
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Calculando a frequência das palavras
all_words = nltk.FreqDist(all_words)

# Objeto para a lista de features das 3.000 palavras mais frequentes
word_features = list(all_words.keys())[:3000]

# Buscando as features
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# Criando o conjunto de features para todos os documentos
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Definindo o dataset de treino
training_set = featuresets[:1900]

# Definindo o dataset de teste
testing_set = featuresets[1900:]

# Criando o classificador e treinando o modelo
classifier = nltk.NaiveBayesClassifier.train(training_set)

# Imprimindo a acurácia
print("\nAcurácia do Modelo: ")
print("Acurácia do Classificador:",(nltk.classify.accuracy(classifier, testing_set))*100)

# Imprimindo as features mais informativas
print("\nFeatures mais informativas: ")
classifier.show_most_informative_features(15)

# Salvando o classificador
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# Carregando o classificador para fazer previsões quando necessário
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()




