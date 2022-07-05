# Extração e Substituição de Caracteres

str = 'Estudando Manipulação de Strings em Python'
print('Substring termina em :', str[:5])

print('Substring começa em :', str[11:] )
print('Substring :',str[5:10])
print('Substring Inversa:', str[-12:-7])

if 'Python' in str:
    print('Encontrei a Palavra Python na String str')

replaced = str.replace('Manipulação', 'Processamento')
print('String Substituída:', replaced)

print('Acessando Cada Caracter na String:')
for s in replaced:
    print(s)