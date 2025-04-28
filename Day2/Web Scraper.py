import requests
from bs4 import BeautifulSoup

URL = "https://example.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Prints page title
