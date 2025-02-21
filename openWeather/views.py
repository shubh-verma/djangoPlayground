# Create your views here.

from django.shortcuts import render
import requests
import datetime
import os

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"


def index(request):
    api_key = os.environ.get("API_KEY", "")

    if request.method != "POST":
        return render(request, "index.html")

    city = request.POST["city"]
    weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city, api_key)
    context = {
        "weather_data1": weather_data1,
        "daily_forecasts1": daily_forecasts1,
    }

    return render(request, "index.html", context)


def fetch_weather_and_forecast(city, api_key):
    weather_response = requests.get(CURRENT_WEATHER_URL.format(city, api_key)).json()
    forecast_response = requests.get(FORECAST_WEATHER_URL.format(city, api_key)).json()
    # weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    # forecast_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}").json()

    # TODO: Create a Serializer to handle JSON to 
    weather_data = {
        "city": city,
        "temperature": round(weather_response["main"]["temp"] - 273.15, 2),
        "description": weather_response["weather"][0]["description"],
        "icon": weather_response["weather"][0]["icon"],
    }

    daily_forecasts = []
    for daily_data in forecast_response["list"][:5]:
        daily_forecasts.append(
            {
                "day": datetime.datetime.fromtimestamp(daily_data["dt"]).strftime("%A"),
                "max_temp": round(daily_data["main"]["temp_max"] - 273.15, 2),
                "min_temp": round(daily_data["main"]["temp_min"] - 273.15, 2),
                "description": daily_data["weather"][0]["description"],
                "icon": daily_data["weather"][0]["icon"],
            }
        )

    return weather_data, daily_forecasts
