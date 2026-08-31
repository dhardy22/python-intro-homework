import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

print("key loaded:", bool(os.getenv("MY_API_KEY")))

url = "https://api.restcountries.com/countries/v5"

query_params = {
    "q": "germ",
    "region": "Europe"
}

r = requests.get(
    url, 
    headers={"Authorization": f'Bearer {os.getenv("MY_API_KEY")}'},
    params=query_params
)

data = r.json()
print(f"Status code: {r.status_code}")

for key, value in data.items():
    print(f"key: {key}: {type(value)}") 

inner = data["data"]
print(inner.keys())
pprint(inner.get("objects", inner)[:1] if isinstance(inner.get("objects"), list) else inner)

