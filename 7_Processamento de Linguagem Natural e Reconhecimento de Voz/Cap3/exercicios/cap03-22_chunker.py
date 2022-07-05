# Chunking

# Chunking é o processo de extrair pequenas frases de um texto

# Em muitos casos, o processamento de linguagem natural é usado para escolher pedaços de frases sem necessariamente analisar a frase completa. 
# No entanto, essas peças podem consistir em várias palavras, então usar espaço em branco para simplesmente quebrar a frase em palavras não é muito útil. 
# Imagine que você está construindo um banco de dados de fatos históricos e uma pequena parte do texto de entrada parece assim:

# Tony Orlando was born on April 3, 1944 in New York City and later moved to New Jersey.

# Nesse caso, provavelmente é útil saber que esse fato envolve uma pessoa, uma data, dois lugares, que consistem em várias palavras que não são 
# muito úteis por si mesmas. Um chunker pode quebrar essa frase em frases que são mais úteis do que palavras individuais, como Tony Orlando e New York City. 
# Identificar termos significativos pode acelerar a busca e produzir melhores resultados.

# Import
import nltk

# Texto
text = "Tony Orlando was born on April 3, 1944 in New York City and later moved to New Jersey."

# Tokenize
sentences = nltk.sent_tokenize(text)

# Loop for para tokenização, Pos-Tagging e Chunking
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(tags)
    print(chunks)
