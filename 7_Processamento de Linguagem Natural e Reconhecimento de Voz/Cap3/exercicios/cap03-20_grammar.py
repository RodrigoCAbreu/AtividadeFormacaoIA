# Criando Sua Própria Gramática

# CFG consiste dos seguintes itens: 

# Um símbolo/token de partida 
# Um conjunto de símbolos/tokens que são terminais 
# Um conjunto de símbolos/tokens que não são terminais 
# Uma regra (ou produção) que define o símbolo/token de início e os possíveis símbolos finais/tokens 
# O símbolo/token pode ser qualquer coisa que seja específica para o idioma que consideramos.

# Por exemplo: 

# No caso da língua inglesa, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t , u, v, w, x, y, z são símbolos/tokens. 
# No caso do sistema de numeração decimal 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 são símbolos/tokens. 

# Geralmente, as regras (ou produções) são escritas na notação Backus-Naur (BNF).

# Imports
import nltk
import string

# Módulo que ajuda a gerar strings a partir do CFG que iremos criar
from nltk.parse.generate import generate


# Definindo o gramática

# A gramática contém as seguintes regras de produção: 

# O símbolo inicial é ROOT 
# O símbolo ROOT pode produzir o símbolo WORD 
# O símbolo WORD pode produzir '' (espaço vazio); esta é uma regra de produção de saída 
# O símbolo WORD pode produzir o símbolo NUMBER seguido do símbolo LETTER 
# O símbolo WORD pode produzir o símbolo LETTER seguido do símbolo NUMBER 

productions = [
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER",
]

# Definindo as regras
digits = list(string.digits)
for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w=digit))

letters = "' | '".join(list(string.ascii_lowercase)[:4])
productions.append("LETTER -> '{w}'".format(w=letters))

# Convertendo as regras para strings
# Procuremos entender para o que esta gramática é. 
# Esta gramática representa o idioma em que existem palavras como 0a, 1a, 2a, a1, a3, e assim por diante.
grammarString = "\n".join(productions)
grammar = nltk.CFG.fromstring(grammarString)
print("\nImprimindo a Gramática Criada")
print(grammar)

# Imprimindo as 15 primeiras palavras geradas pela nossa gramática
print("\n")   
for sentence in generate(grammar, n=15, depth=15):
    palindrome = "".join(sentence).replace(" ", "")
    print("Palavra Gerada: {}, Tamanho : {}".format(palindrome, len(palindrome)))

print("\n")    
