import os

# Fazendo a leitura de um arquivo se texto
with open(os.path.join("data", "frases.txt"), "r") as f:
    text = f.read()
    print(text)