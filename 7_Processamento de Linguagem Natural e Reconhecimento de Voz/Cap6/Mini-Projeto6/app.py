# Mini-Projeto 6 - App Web Para Busca de Palavras

# Imports
import json
from flask import Flask, render_template, request
from difflib import get_close_matches as gcm

# Carrega os dados
dicionario = json.load(open('dicionario.json'))

# Cria a app
app = Flask(__name__)

# Define qual página html será aberta ao abrir a raiz (/) da aplicação
@app.route('/')
def home():
    return render_template("index.html")

# Página que mostra o resultado de uma busca
@app.route('/busca/')
@app.route('/busca/', methods = ['POST'])
def busca():

    # Obtém a palavra digitada no formulário
    palavra = request.form['search']

    # Converte a palavra em minúsculo
    palavra = palavra.lower()

    # Saída
    output = ''

    # Verifica se a palavra está no dicionário
    if palavra in dicionario:
        output = dicionario[palavra]
    elif palavra.title() in dicionario:
        output = dicionario[palavra.title()]
    elif palavra.upper() in dicionario:
        output = dicionario[palavra.upper()]
    elif len(gcm(palavra, dicionario.keys())) > 0:
        response = " %s " % gcm(palavra, dicionario.keys())[0]
        output = dicionario[gcm(palavra, dicionario.keys())[0]]

        if type(output) == list:
            for item in output:
                return render_template("busca.html", bot = [response, item])
        else:
            return render_template("busca.html", bot = [response, output])

    else:
        output = "Essa palavra não existe ou não pode ser encontrada."

    # Se a saída for uma lista chamamos a página resultado
    if output:
        if type(output) == list:
            for item in output:
                return render_template("resultado.html", bot = item)
        else:
            return render_template("resultado.html", bot = output)

# Execução do programa
if __name__=="__main__":
    app.run(debug = False)
