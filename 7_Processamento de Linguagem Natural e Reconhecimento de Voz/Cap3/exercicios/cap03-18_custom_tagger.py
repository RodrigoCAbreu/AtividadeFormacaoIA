# Custom Tagger

# Import
import nltk

# Recebe um texto como input e imprime cada palavra com uma tag default
def learnDefaultTagger(simpleSentence):
    # Tokenização
    wordsInSentence = nltk.word_tokenize(simpleSentence)

    # Etiquetador
    tagger = nltk.DefaultTagger("NN")

    # Aplicando o Etiquetador ao conjunto de palavras
    posEnabledTags = tagger.tag(wordsInSentence)
    print("\nPalavras com a tag default")
    print(posEnabledTags)

# Recebe um texto como input e imprime a lista de tokens com as tags definidas usando expressões regulares
def learnRETagger(simpleSentence):
    customPatterns = [
        (r'.*ing$', 'ADJECTIVE'),             
        (r'.*ly$', 'ADVERB'),                 
        (r'.*ion$', 'NOUN'),                  
        (r'(.*ate|.*en|is)$', 'VERB'),        
        (r'^an$', 'INDEFINITE-ARTICLE'),      
        (r'^(with|on|at)$', 'PREPOSITION'),   
        (r'^\-?[0-9]+(\.[0-9]+)$', 'NUMBER'), 
        (r'.*$', None),
    ]

    # Etiquetador
    tagger = nltk.RegexpTagger(customPatterns)

    # Tokenização
    wordsInSentence = nltk.word_tokenize(simpleSentence)

    # Aplicando o Etiquetador ao conjunto de palavras
    posEnabledTags = tagger.tag(wordsInSentence)
    print("\nPalavras com a tag definida por expressões regulares")
    print(posEnabledTags)

# Recebe um texto como input e imprime a lista de tokens com as tags definidas usando expressões regulares
def learnLookupTagger(simpleSentence):
    mapping = {
        '.': '.', 'place': 'NN', 'on': 'IN',
        'earth': 'NN', 'Mysore' : 'NNP', 'is': 'VBZ',
        'an': 'DT', 'amazing': 'JJ'
    }

    # Etiquetador
    tagger = nltk.UnigramTagger(model=mapping)

    # Tokenização
    wordsInSentence = nltk.word_tokenize(simpleSentence)

    # Aplicando o Etiquetador ao conjunto de palavras
    posEnabledTags = tagger.tag(wordsInSentence)
    print("\nPalavras com a tag definida por mapeamento")
    print(posEnabledTags)

# Executa o programa
if __name__ == '__main__':
    testSentence = "London is an amazing place on earth. I have London 10 times."
    learnDefaultTagger(testSentence)
    learnRETagger(testSentence)
    learnLookupTagger(testSentence)
    print("\n")
