import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()  # reads MY_API_KEY from a local .env file, if one exists

url = "https://api.restcountries.com/countries/v5"


def fetch_countries():
    """Fetch every country from the API, paging through results.

    The API returns results in pages (25 per page by default) along with
    a "meta" block describing the total count and whether more pages
    remain. This loops through all pages, collecting every country
    object into a single list, and stops once the API reports there's
    no more data (meta["more"] is False).

    Returns:
        A dict shaped like {"data": {"objects": [...]}} containing every
        country object combined across all pages, or None if the request
        failed (network error or non-200 status code).
    """
    all_objects = []
    offset = 0

    while True:
        try:
            r = requests.get(
                url,
                headers={"Authorization": f'Bearer {os.getenv("MY_API_KEY")}'},
                params={"offset": offset}
            )
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

        if r.status_code != 200:
            print(f"API returned status {r.status_code}")
            return None

        payload = r.json()["data"]
        all_objects.extend(payload["objects"])

        # Stop paging once the API says there's nothing left to fetch
        if not payload["meta"].get("more", False):
            break

        offset += payload["meta"]["limit"]  # advance by whatever page size the API actually used

    # Note: only "objects" is carried forward here — "meta" applied to a
    # single page and doesn't represent the combined result, so it's
    # intentionally dropped rather than merged from the last page.
    return {"data": {"objects": all_objects}}


def parse_countries(raw_data):
    """Reshape the raw API response into a simple, flat list of dicts.

    The raw API response nests everything under {"data": {"objects": all_objects}}, and uses
    field names (names.common, capitals[0].name) that doesn't match the structure that 
    the rest of the program works with. This function pulls
    just the fields we need into a flat, predictable shape.

    Args:
        raw_data: the dict returned by fetch_countries().

    Returns:
        A list of dicts, each shaped like:
        {"name": ..., "capital": ..., "region": ..., "population": ...}
    """
    countries = []
    for c in raw_data["data"]["objects"]:
        # Some countries have no capital listed at all, so guard against
        # an empty list before indexing into it.
        capitals = c.get("capitals", [])
        capital = capitals[0]["name"] if capitals else "N/A"

        countries.append({
            "name": c["names"]["common"],
            "capital": capital,
            "region": c.get("region", "N/A"),
            "population": c.get("population", 0)
        })
    return countries


# Fetch and parse the full country list once, at startup. Every menu
# option below works off this local list — no further API calls happen
# after this point.
raw = fetch_countries()
if raw is None:
    print("Could not load country data. Exiting.")
    exit()

countries = parse_countries(raw)


def search_by_name(countries, term):
    """Print every country whose name contains the given search term.

    The match is case-insensitive and a partial match (a term of "land"
    will match "Iceland", "Ireland", "Finland", etc.).

    Args:
        countries: the flat list of country dicts from parse_countries().
        term: the search string entered by the user.
    """
    matches = [c for c in countries if term.lower().strip() in c["name"].lower().strip()]
    matches.sort(key=lambda c: c["population"], reverse=True)
    for c in matches:
        print(f'{c["name"]} — Capital: {c["capital"]} | Region: {c["region"]} | Population: {c["population"]:,}')


def filter_by_region(countries, region):
    """Print every country in a given region, sorted by population.

    The region match is case-insensitive and must match exactly (not a
    partial match like search_by_name). Results are sorted largest
    population first.

    Args:
        countries: the flat list of country dicts from parse_countries().
        region: the region name entered by the user (e.g. "Europe").
    """
    matches = [c for c in countries if region.lower().strip() in c["region"].lower().strip()]
    matches.sort(key=lambda c: c["population"], reverse=True)
    for c in matches:
        print(f'{c["name"]} — Population: {c["population"]:,}')


# print(f"Loaded {len(countries)} countries")

# Main menu loop: keeps prompting until the user chooses to quit.
def show_menu():
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")
    return choice
    
while True:
    choice = show_menu()
    if choice == "1":
        name = input("Enter country name: ")
        search_by_name(countries, name)
    elif choice == "2":
        region = input("Enter region: ")
        filter_by_region(countries, region)
    elif choice == "3":
        print("Goodbye!")
        break