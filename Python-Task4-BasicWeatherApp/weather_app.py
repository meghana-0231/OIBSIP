import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key


print("\n====== WEATHER APP ======")

while True:
    try:
        location = input(
            "\nEnter city name or ZIP code (or type 'exit' to quit): "
        ).strip()

        # Exit option
        if location.lower() == "exit":
            print("\nThank you for using Weather App!")
            break

        # Input validation
        if not location:
            print("Location cannot be empty. Please try again.")
            continue

        # Choose city or ZIP code
        if location.isdigit():
            params = {
                "zip": f"{location},IN",
                "appid": API_KEY,
                "units": "metric"
            }
        else:
            params = {
                "q": location,
                "appid": API_KEY,
                "units": "metric"
            }

        # API request
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params,
            timeout=10
        )

        data = response.json()

        # Display weather information
        if data["cod"] == 200:

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32

            print("\n------ Weather Report ------")
            print("City:", data["name"])
            print("Temperature:", temperature_c, "°C")
            print("Temperature:", temperature_f, "°F")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
            print("Wind Speed:", data["wind"]["speed"], "m/s")
            print("----------------------------")

        else:
            print(
                "Error:",
                data.get("message", "Unable to fetch weather data.")
            )

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print(
            "Error: Network error occurred. "
            "Please check your internet connection and try again."
        )

    except ValueError:
        print(
            "Error: Invalid response received from the weather service. "
            "Please try again later."
        )