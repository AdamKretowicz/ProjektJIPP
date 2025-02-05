from pickletools import read_uint1

import requests
from dotenv import load_dotenv
import os


def get_weather(city):
    load_dotenv()  # Wczytuje zmienne z pliku .env
    # 0d4ab13fe19a263cf9918a35b01d7f89  <- API KEY do sprawdzenia
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pl"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if not response.ok:
            return {"błąd": data["message"]}

        return {
            "Miasto": data["name"],
            "Temperatura": f"{data["main"]["temp"]}°C",
            "Wilgotność": f"{data["main"]["humidity"]}%",
            "Ciśnienie": f"{data["main"]["pressure"]} hPa",
            "Opis": data["weather"][0]["description"].capitalize()
        }
    except:
        return {"błąd": "Błąd serwera"}


if __name__ == "__main__":
    city = input("Podaj nazwę miasta: ")
    weather = get_weather(city)
    if not weather:
        print("Brak danych")
        exit()
    for key, value in weather.items():
        print(f"{key}: {value}")