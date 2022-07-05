# Expressões Regulares

# Usando caracteres coringa:

# . - qualquer caractere

# Import
import re

def text_match(text, patterns):
        if re.search(patterns,  text):
                return 'Encontrei correspondência!'
        else:
                return('Não Encontrei correspondência!')

print("\n")
print("Padrão para testar início e fim de uma string")
# Este padrão ^a.*c$ significa: padrão que comece com a letra, seguido de zero ou mais quaisquer carateres e terminando com a letra c
print(text_match("abjjuuggevevzwebc", "^a.*c$"))

print("\n")
print("Padrão para verificar se uma palavra está no começo do texto")
# Este padrão ^\w+ significa: padrão que comece (^) com qualquer caractere alfa-numérico (\w) e uma ou mais ocorrências (+)
print(text_match("José come torta, Maria come ervilhas!", "^\w+"))

print("\n")
print("Padrão para verificar se uma palavra está no final do texto, seguida de pontuação")
# Este padrão \w+\S*?$ significa: padrão que tenha uma ou mais ocorrências alfa-numéricas (\w), 
# seguida de zero ou mais ocorrências de pontuação (\S) e que esteja no final do texto de input ($)
print(text_match("José come torta, Maria come ervilhas!", "\w+\S*?$"))

print("\n")	
print("Encontrar uma palavra que contenha um caracter específico (letra u), mas que NÃO esteja no começo ou final de uma palavra do texto de input")
print(text_match("José come torta, Maria come ervilhas!", "\Bu\B"))
print(text_match("Josué come torta, Maria come ervilhas!", "\Bu\B"))
print("\n")	