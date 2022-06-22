# Acessando Corpora

# Import
from nltk.corpus import reuters

# Visualizando os arquivos no Corpora
files = reuters.fileids()
print(files)

# Acessando um arquivo
words16097 = reuters.words(['test/16097'])
print(words16097)

# Acessando um número específico de palavras em um arquivo
words20 = reuters.words(['test/16097'])[:20]
print(words20)

# O Corpora não é apenas uma lista de arquivos, mas uma hierarquia categorizada de 90 tópicos.
# Cada tópico tem vários arquivos associados. 
# Quando acessamos um tópicos estamos na verdade acessando os arquivos associados ao tópico.
reutersGenres = reuters.categories()
print(reutersGenres)

# Acessando 2 tópicos e imprimindo as palavras
for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print()
