def welcome_message():
    print("Welcome to the Weather Forecast Application!")

def get_city_name():
    return input("Please enter the city name for the weather forecast: ")

def fetch_weather_data(city):
    # Hardcoded weather data for demonstration purposes
    weather_data = {
        "London": {"temperature": 15, "condition": "sunny", "wind_speed": 5, "humidity": 60},
        "New York": {"temperature": 20, "condition": "rainy", "wind_speed": 10, "humidity": 70},
        "Tokyo": {"temperature": 18, "condition": "cloudy", "wind_speed": 7, "humidity": 65},
        "Sydney": {"temperature": 25, "condition": "sunny", "wind_speed": 12, "humidity": 55},
        "Paris": {"temperature": 17, "condition": "windy", "wind_speed": 8, "humidity": 50}
    }
    return weather_data.get(city, None)

def display_weather_data(city, weather):
    if weather:
        print(f"\nWeather forecast for {city}:")
        print(f"Current temperature: {weather['temperature']}°C")
        print(f"Weather conditions: {weather['condition']}")
        print(f"Wind speed: {weather['wind_speed']} km/h")
        print(f"Humidity: {weather['humidity']}%")
    else:
        print(f"Sorry, weather data for {city} is not available try again.")
        return main() 


def main():
    welcome_message()
    city = get_city_name()
    weather = fetch_weather_data(city)
    display_weather_data(city, weather)

if __name__ == "__main__":
    main()


