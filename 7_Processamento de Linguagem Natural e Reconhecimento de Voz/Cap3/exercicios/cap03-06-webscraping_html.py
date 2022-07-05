# Extraindo Texto de Páginas HTML

# Import
from bs4 import BeautifulSoup

# Arquivo
html_doc = open('index.html', 'r').read()

# Parser
soup = BeautifulSoup(html_doc, 'html.parser')

print('Texto HTML Completo Stripped:')
print(soup.get_text())

print('Acessando o texto na tag <title> :', end=' ')
print(soup.title)

print('Acessando o texto na tag <H1> :', end=' ')
print(soup.h1.string)

print('Acessando a propriedade na tag <img> :', end=' ')
print(soup.img['alt'])

print('\nAcessando todas as ocorrências da tag <p> :')
for p in soup.find_all('p'):
    print(p.string)