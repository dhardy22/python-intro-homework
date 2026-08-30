import requests

url = "https://api.agify.io/?name=michael"
response = requests.get(url)

data = response.json()

print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(data.get("birthday", "Birthday: Not available"))