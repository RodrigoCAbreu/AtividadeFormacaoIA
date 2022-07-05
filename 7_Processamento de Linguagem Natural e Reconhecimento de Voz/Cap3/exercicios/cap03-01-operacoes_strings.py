# Operações com Strings

# Criando lista de nomes e sentença
namesList = ['Eric','Bob','Marc','Tim']
sentence = 'Meu cachorro está dormindo no sofá'

# Incluindo ; entre os nomes da lista
names = ';'.join(namesList)
print(type(names), ':', names)

# Transformando uma frase em uma lista de palavras
wordList = sentence.split(' ')
print((type(wordList)), ':', wordList)

# Operações matemáticas com strings
additionExample = 'juiz' + 'juiz' + 'juiz'
multiplicationExample = 'juiz' * 2
print('Adição de Texto :', additionExample)
print('Multiplicação de Texto :', multiplicationExample)

# Extraindo caracteres de um texto
str = 'Python NLTK'
print(str[1])
print(str[-3])