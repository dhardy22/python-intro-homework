import requests

url = "https://api.agify.io/?name=michael"

try:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Request failed: status {response.status_code}")
    else:
        data = response.json()
        # work with data here
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")


print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(data.get("birthday", "Birthday: Not available"))  