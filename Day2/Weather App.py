import requests

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
data = response.json()

if data["cod"] == 200:
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("City not found!")
