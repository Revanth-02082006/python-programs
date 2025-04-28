import requests

API_URL = "https://api.example.com/stock"
symbol = input("Enter stock symbol: ")
response = requests.get(f"{API_URL}?symbol={symbol}")
data = response.json()

print(f"Stock Price of {symbol}: {data['price']}")
