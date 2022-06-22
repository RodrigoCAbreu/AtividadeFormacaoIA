# Tokenization
# Processo de dividir uma string em listas de pedaços ou "tokens". 
# Um token é uma parte inteira. Por exemplo: uma palavra é um token em uma sentença. Uma sentença é um token em um parágrafo.

# Imports
from nltk.tokenize import sent_tokenize, word_tokenize

# Texto
frase = "Hora de começar com o processamento de linguagem natural. Python vai facilitar nossa vida!"

# Tokenization em sentenças
sent_tokens = sent_tokenize(frase)
print(sent_tokens)

# Tokenization em palavras
word_tokens = word_tokenize(frase)
print(word_tokens)
print(word_tokenize("can't"))

# Usando tokenizers customizados
from nltk.tokenize import TreebankWordTokenizer

# TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize('Hello World.'))

# Tokenization por Pontuação
from nltk.tokenize import WordPunctTokenizer

tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize("Can't is a contraction."))

# Tokenization por expressões regulares
from nltk.tokenize import RegexpTokenizer

# RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
print(tokenizer.tokenize("Can't is a contraction."))

# Tokenization por expressões regulares
from nltk.tokenize import regexp_tokenize

# regexp_tokenize
print(regexp_tokenize("Can't is a contraction.", "[\w']+"))

tokenizer = RegexpTokenizer('\s+', gaps = True)
print(tokenizer.tokenize("Can't is a contraction."))


