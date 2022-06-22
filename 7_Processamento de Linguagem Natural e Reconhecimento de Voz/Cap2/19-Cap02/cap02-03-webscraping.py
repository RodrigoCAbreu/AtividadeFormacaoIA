import requests
import json

# Obtendo dados de uma API REST
r = requests.get("https://quotes.rest/qod.json")
res = r.json()
print(json.dumps(res, indent=4))

# Extraindo objeto e campo relevante 
q = res["contents"]["quotes"][0]
print(q["quote"], "\n--", q["author"])