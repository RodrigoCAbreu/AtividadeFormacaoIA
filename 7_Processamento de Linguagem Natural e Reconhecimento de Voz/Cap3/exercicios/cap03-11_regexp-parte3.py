# Expressões Regulares

# Imports
import re

# Texto
text = 'José come torta, Maria come ervilhas!'

# Lista de padrões
patterns = [ 'José', 'Torta', 'ervilhas' ]

# Busca por strings literais na frase
print("\n")
for pattern in patterns:
    print('Buscando por "%s" em "%s" ' % (pattern, text),)
    if re.search(pattern,  text):
        print('Encontrei!')
        print("\n")
    else:
        print('Não Encontrei!')
        print("\n")


# Texto
text = 'Um festival de luzes pode ser visto sempre que ocorre um festival de fogos de artifício!'

# Padrão
pattern = 'festival'

# Buscando uma string e identificando sua localização
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Encontrado "%s" em %d:%d' % (text[s:e], s, e))
    print("\n")