# Expressões Regulares
# https://docs.python.org/3/reference/lexical_analysis.html#literals

# Imports
import re

# Substituir palavras
street = '42 Sunshine Road'
print(re.sub('Road', 'Rd', street))

# Encontrar palavras com comprimento específico
text = 'Cada cicatriz que temos é a confirmação de que uma ferida sara. Cicatrizes são marcas de superação que só um verdadeiro guerreiro possui!'
print(re.findall(r"\b\w{6}\b", text))

# Prefixo r (raw)
print (re.sub(r'(\b\w+)(\s+\1\b)+', r'\1', 'hello     there      there'))
print (re.sub('(\\b\\w+)(\\s+\\1\\b)+', '\\1', 'hello     there      there'))