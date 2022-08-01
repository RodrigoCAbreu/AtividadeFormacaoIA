# Named Entity Recognition

# Imports
import nltk
import time

contentArray =['A Sadia vem aumentando sua participação no mercado de forma significativa.',
               'O Brasil é o produtor de café número 1 do mundo e fornece cerca de 1/3 do café do mundo inteiro!',
               'A Starbucks ainda vê forte crescimento de vendas nos Estados Unidos, e pretende continuar crescendo.',]



# Função para processar cada frase da lista de sentenças
def processLanguage():
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print(tagged)

            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()

            time.sleep(1)

    except Exception as e:
        print (str(e))
        

processLanguage()
		