# Expressões Regulares

# Imports
import re

# URL
url = "http://www.telegraph.co.uk/football/2018/01/16/jose-mourinho-close-signing-new-contract-manchester-united"

# Busca pela data
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/'

# Print da Data
print("Data encontrada na URL :", re.findall(date_regex, url))
