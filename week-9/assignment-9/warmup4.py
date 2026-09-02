import requests

url = "https://thisurldoesnotexist.example.com"

try:
    r = requests.get(
        url
    )
    print("Success!")
except requests.exceptions.RequestException as e:
    print("Error: Could not reach the server. Check your connection and try again:")
    