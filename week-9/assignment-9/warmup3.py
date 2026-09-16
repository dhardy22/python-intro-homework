import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

url = "https://api.restcountries.com/countries/v5"
params = {
    "region": "Europe"
}

r = requests.get(
    url,
    headers={"Authorization": f'Bearer {os.getenv("MY_API_KEY")}'},
    params=params
)

print(r.request.url)          # the actual URL that was sent
print(f"Status code: {r.status_code}")

data = r.json()
print(type(data))

countries = data["data"]["objects"]

print(len(countries))

for country in countries[:10]:
    print(country["names"]["common"])