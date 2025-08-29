def get_weather(city):
    # Mock weather data
    weather_data = {
        "delhi": {"temp": 28, "condition": "Sunny", "humidity": 45},
        "mumbai": {"temp": 32, "condition": "Cloudy", "humidity": 70},
        "kolkata": {"temp": 30, "condition": "Rainy", "humidity": 80},
        "chennai": {"temp": 34, "condition": "Hot", "humidity": 75},
        "bangalore": {"temp": 26, "condition": "Pleasant", "humidity": 60}
    }
    
    city = city.lower()
    if city in weather_data:
        return weather_data[city]
    else:
        return None

def main():
    print("🌤️  Welcome to Weather App!")
    print("Available cities: Delhi, Mumbai, Kolkata, Chennai, Bangalore")
    
    city = input("\nEnter city name: ")
    weather = get_weather(city)
    
    if weather:
        print(f"\n📊 Weather in {city.capitalize()}:")
        print(f"🌡️  Temperature: {weather['temp']}°C")
        print(f"☁️  Condition: {weather['condition']}")
        print(f"💧 Humidity: {weather['humidity']}%")
    else:
        print("❌ City not found in database!")

if __name__ == "__main__":
    main()

