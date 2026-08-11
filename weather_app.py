import requests
import json

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
print("\n------ Weather Report ------")

while True:
    city = input("\nEnter city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        print("\n===================================")
        print("🌤 Thank you for using Weather App!")
        print("Have a wonderful day! 😊")
        print("===================================")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        print("\n------ Weather Report ------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("Error:", data.get("message", "Unable to fetch weather data."))
