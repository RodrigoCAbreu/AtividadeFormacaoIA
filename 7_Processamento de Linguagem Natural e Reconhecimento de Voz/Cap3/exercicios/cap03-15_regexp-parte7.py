# Expressões Regulares

# Import
import re

# Função para stem
def stem(word):
    splits = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', word)
    stem = splits[0][0]
    return stem

# Texto
raw = "Keep your friends close, but your enemies closer."

# Tokenização
tokens = re.findall(r'\w+|\S\w*', raw)
print(tokens)

# Stemming
for t in tokens:
    print("'"+stem(t)+"'")