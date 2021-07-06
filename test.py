import requests
import json
res = requests.get(f'https://api.exchangeratesapi.io/latest?base=RUB&symbols=USD')
print(json.loads(res.content)['rate']['USD'])