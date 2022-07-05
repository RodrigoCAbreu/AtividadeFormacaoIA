# Expressões Regulares

# Import
import re

# Texto
texto = "I am big! It's the picture that got small."

# Criando um tokenizer personalizado
print("\n")
print("Opção 1 (tokenização por espaço):")
print(re.split(r' +', texto))

print("\n")
print("Opção 2 (tokenização por 'não palavras'):")
print(re.split(r'\W+', texto))

print("\n")
print("Opção 3 (tokenização preservando os acentos):")
print(re.findall(r'\w+|\S\w*', texto))
print("\n")