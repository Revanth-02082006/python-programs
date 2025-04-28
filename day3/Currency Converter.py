import requests

BASE_URL = "https://api.exchangerate-api.com/v4/latest/USD"
amount = float(input("Enter amount: "))
currency = input("Enter target currency: ").upper()

rates = requests.get(BASE_URL).json()["rates"]
if currency in rates:
    converted = amount * rates[currency]
    print(f"Converted Amount: {converted} {currency}")
else:
    print("Invalid Currency Code!")
