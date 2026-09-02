import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
url = "https://api.restcountries.com/countries/v5"


def fetch_countries():
    """Hits the API once. Returns raw JSON on success, None on failure."""
    try:
        r = requests.get(url, headers={"Authorization": f'Bearer {os.getenv("MY_API_KEY")}'})
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    if r.status_code != 200:
        print(f"API returned status {r.status_code}")
        return None

    return r.json()



def parse_countries(raw_data):
    """Takes the raw API response, returns a flat list of dicts:
    [{"name": ..., "capital": ..., "region": ..., "population": ...}, ...]
    """
    countries = []
    for c in raw_data["data"]["objects"]:
        capitals = c.get("capitals", [])
        capital = capitals[0]["name"] if capitals else "N/A"

        countries.append({
            "name": c["names"]["common"],
            "capital": capital,
            "region": c.get("region", "N/A"),
            "population": c.get("population", 0)
        })
    return countries

raw = fetch_countries()
if raw is None:
    print("Could not load country data. Exiting.")
    exit()

countries = parse_countries(raw)

def search_by_name(countries, term):
    matches = [c for c in countries if term.lower().strip() in c["name"].lower().strip()]
    for c in matches:
        print(f'{c["name"]} — Capital: {c["capital"]} | Region: {c["region"]} | Population: {c["population"]:,}')

def filter_by_region(countries, region):
    matches = [c for c in countries if c["region"].lower().strip() == region.lower().strip()]
    matches.sort(key=lambda c: c["population"], reverse=True)
    for c in matches:
        print(f'{c["name"]} — Population: {c["population"]:,}')


print(f"Loaded {len(countries)} countries")

print(raw["data"]["meta"])

while True:
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Enter country name: ")
        search_by_name(countries, name)


    if choice == "2":
        region = input("Enter region: ")
        filter_by_region(countries, region)


    if choice == "3":
        print("Goodbye!")
        break





# print(r.request.url)          # the actual URL that was sent
# print(f"Status code: {r.status_code}")

# data = r.json()
# print(type(data))

# countries = data["data"]["objects"]

# print(len(countries))

# for country in countries[:10]:
#     print(country["names"]["common"])