# Expressões Regulares

# Usando caracteres coringa:

# ? - zero ou um
# * - zero ou mais
# + - um ou mais

# Import
import re

# Função
def text_match(text, patterns):
        if re.search(patterns,  text):
                return 'Encontrei correspondência!'
        else:
                return('Não Encontrei correspondência!')

print("\n")
print("Caracter Coringa ?:")
print(text_match("ac", "ab?"))
print(text_match("abc", "ab?"))
print(text_match("abbc", "ab?"))
print(text_match("a", "ab?"))
print(text_match("b", "ab?"))
print("\n")

print("Caracter Coringa *:")
print(text_match("ac", "ab*"))
print(text_match("abc", "ab*"))
print(text_match("abbc", "ab*"))
print(text_match("a", "ab*"))
print(text_match("b", "ab*"))
print("\n")

print("Caracter Coringa +:")
print(text_match("ac", "ab+"))
print(text_match("abc", "ab+"))
print(text_match("abbc", "ab+"))
print(text_match("a", "ab+"))
print(text_match("b", "ab+"))
print("\n")

print("Outros Exemplos:")

# Uma letra a seguida exatamente por duas letras b
print(text_match("abbc", "ab{2}"))
print(text_match("abc", "ab{2}"))
print("\n")


