import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key   

print("\n------ Weather Report ------")

while True:
    try:
        location = input(
            "\nEnter city name or ZIP code (or type 'exit' to quit): "
        ).strip()

        if location.lower() == "exit":
            print("\n==============================")
            print("☁ Thank you for using Weather App!")
            print("Have a wonderful day! 😊")
            print("==============================")
            break

        # Empty input validation
        if not location:
            print("Error: City name or ZIP code cannot be empty.")
            continue

        # Create API URL for ZIP code or city
        if location.isdigit():
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?zip={location},IN&appid={API_KEY}&units=metric"
            )
        else:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={location}&appid={API_KEY}&units=metric"
            )

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32

            print("\n------ Weather Report ------")
            print("City:", data["name"])
            print("Temperature:", round(temperature_c, 2), "°C")
            print("Temperature:", round(temperature_f, 2), "°F")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
            print("Wind Speed:", data["wind"]["speed"], "m/s")

        elif response.status_code == 404:
            print("Error: City or ZIP code not found.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        else:
            print(
                "Error:",
                data.get("message", "Unable to fetch weather data.")
            )

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection problem.")

    except requests.exceptions.RequestException:
        print("Error: Unable to connect to the weather service.")

    except ValueError:
        print("Error: Invalid response received from the weather service.")