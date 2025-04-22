import requests
from bs4 import BeautifulSoup
city = input("Enter city: ")
url = f"https://www.weather.com/weather/today/l/{city}"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text)
