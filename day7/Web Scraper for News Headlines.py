import requests
from bs4 import BeautifulSoup

URL = "https://example.com/news"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")
for headline in headlines:
    print(headline.text)
