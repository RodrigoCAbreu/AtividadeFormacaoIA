import os
import pandas as pd

# Extrai coluna de texto do dataframe
df = pd.read_csv(os.path.join("data", "news.csv"))

# Converte o texto em lowercase
df['title'] = df['title'].str.lower()
resultado = df.head()[['publisher', 'title']]
print(resultado)