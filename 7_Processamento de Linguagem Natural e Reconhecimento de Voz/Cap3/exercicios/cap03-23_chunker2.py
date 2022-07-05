# Criando Seu Próprio Chunker

# Import
import nltk

# Texto
text = "Elon Musk is the CEO of a Company. He is very powerful public speaker also."

# Gramática
grammar = '\n'.join([
    'NP: {<DT>*<NNP>}',
    'NP: {<JJ>*<NN>}',
    'NP: {<NNP>+}',
])

# Tokenização
sentences = nltk.sent_tokenize(text)

# Chunking
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunkparser = nltk.RegexpParser(grammar)
    result = chunkparser.parse(tags)
    print(result)
