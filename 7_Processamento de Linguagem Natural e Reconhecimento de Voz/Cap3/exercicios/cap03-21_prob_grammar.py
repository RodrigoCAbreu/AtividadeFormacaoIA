# Imports

import nltk
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD [1.0]",
    "WORD -> P1 [0.25]",
    "WORD -> P1 P2 [0.25]",
    "WORD -> P1 P2 P3 [0.25]",
    "WORD -> P1 P2 P3 P4 [0.25]",
    "P1 -> 'A' [1.0]",
    "P2 -> 'B' [0.5]",
    "P2 -> 'C' [0.5]",
    "P3 -> 'D' [0.3]",
    "P3 -> 'E' [0.3]",
    "P3 -> 'F' [0.4]",
    "P4 -> 'G' [0.9]",
    "P4 -> 'H' [0.1]",
]

# Converte o objeto para string
grammarString = "\n".join(productions)

# Cria a PCFG
grammar = nltk.PCFG.fromstring(grammarString)

# Print da Gramática
print("\nImprimindo a Gramática Criada")
print(grammar)

# Imprimindo as 10 primeiras palavras geradas pela nossa gramática
for sentence in generate(grammar, n=10, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("String : {}, Tamanho : {}".format(palindrome, len(palindrome)))

print("\n")  