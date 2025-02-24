# Create your views here.

from django.shortcuts import render
from openWeatherREST.serializers import WeatherResponseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import datetime
import os

# CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"


@api_view(["GET", "POST"])
def open_weather_REST(request):
    api_key = os.environ.get("API_KEY", "")

    city = request.query_params.get("q")
    daily_forecasts = fetch_weather_and_forecast(city, api_key)
    if daily_forecasts and daily_forecasts.is_valid():
        return Response((daily_forecasts.data), status=200)


def fetch_weather_and_forecast(city, api_key):
    # weather_response = requests.get(CURRENT_WEATHER_URL.format(city, api_key)).json()
    forecast_response = requests.get(FORECAST_WEATHER_URL.format(city, api_key))
    # weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    # forecast_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}").json()

    # TODO: Create a Serializer to handle JSON to
    return WeatherResponseSerializer(data=forecast_response.json())

    # return weather_data, daily_forecasts
