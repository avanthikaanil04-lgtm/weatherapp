import requests

API_KEY = "f5722a1cfb4eb51ca40d4cb7998934af"

print("🌦 Simple Weather App 🌦")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\n📍 City:", city.title())
        print("🌡 Temperature:", temperature, "°C")
        print("💧 Humidity:", humidity, "%")
        print("🌥 Condition:", description.capitalize())
    else:
        print("❌ City not found. Please try again.")

except Exception as e:
    print("⚠ Something went wrong.")
    print("Error:", e)
