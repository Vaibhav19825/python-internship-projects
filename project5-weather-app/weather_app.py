# Project 5 - Weather App with Live OpenWeather API
import os
import time
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/"
cache = {}           
cache_seconds = 600  


def load_api_key():
    
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, ".env")
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("API_KEY="):
                    return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return None


def call_api(endpoint, city, key):
    params = {"q": city, "appid": key, "units": "metric"}
    try:
        response = requests.get(BASE_URL + endpoint, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Could not connect. Check your internet and try again.")
        return None

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Invalid API key. A new key can take a while to start working.")
    elif response.status_code == 404:
        print("City not found. Please check the spelling.")
    else:
        print("Something went wrong. Error code:", response.status_code)
    return None


def get_weather(city, key):
    name = city.lower()

    
    if name in cache:
        saved_time, data = cache[name]
        if time.time() - saved_time < cache_seconds:
            return data

    current = call_api("weather", city, key)
    if current is None:
        return None
    forecast = call_api("forecast", city, key)
    if forecast is None:
        return None

    data = (current, forecast)
    cache[name] = (time.time(), data)
    return data


def show_weather(current, forecast):
    city = current["name"]
    country = current["sys"]["country"]
    temp = current["main"]["temp"]
    feels = current["main"]["feels_like"]
    humidity = current["main"]["humidity"]
    wind = current["wind"]["speed"]
    description = current["weather"][0]["description"]

    print("\n==============================")
    print("Weather in", city + ",", country)
    print("==============================")
    print("Condition  :", description.title())
    print("Temperature:", round(temp, 1), "C (feels like", round(feels, 1), "C)")
    print("Humidity   :", humidity, "%")
    print("Wind speed :", wind, "m/s")

    print("\nForecast (12:00 UTC each day):")
    for item in forecast["list"]:
        date_time = item["dt_txt"]
        if date_time.endswith("12:00:00"):
            day = date_time[:10]
            temperature = round(item["main"]["temp"], 1)
            desc = item["weather"][0]["description"]
            print(day, "-", temperature, "C,", desc)


def main():
    key = load_api_key()
    if key is None or key == "":
        print("API key not found. Create a .env file with: API_KEY=your_key")
        return

    print("Welcome to the Weather App!")
    while True:
        city = input("\nEnter a city name (or q to quit): ").strip()
        if city.lower() == "q":
            print("Goodbye!")
            break
        if city == "":
            print("Please type a city name.")
            continue

        result = get_weather(city, key)
        if result is not None:
            show_weather(result[0], result[1])


main()