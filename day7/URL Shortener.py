import requests

API_URL = "https://api.example.com/shorten"
long_url = input("Enter URL: ")
response = requests.post(API_URL, json={"url": long_url})
short_url = response.json()["shortened_url"]

print(f"Shortened URL: {short_url}")
