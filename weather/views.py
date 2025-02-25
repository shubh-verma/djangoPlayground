# Create your views here.

from .serializers import WeatherSerializer, ForecastResponseSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import os

FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


@api_view(["GET", "POST"])
def weather(request):
    api_key = os.environ.get("API_KEY", "")

    city = request.query_params.get("q")

    if not city:
        return Response({"error": "City is required"}, status=400)
    current_weather = fetch_weather(city, api_key)

    if current_weather and current_weather.is_valid():
        return Response(current_weather.data, status=200)
    return Response({"error": "Invalid response from weather API"}, status=500)


def fetch_weather(city, api_key):
    weather_response = requests.get(CURRENT_WEATHER_URL.format(city, api_key))
    return WeatherSerializer(data=weather_response.json())


class WeatherAPIView(APIView):
    def get(self, request, format=None):
        api_key = os.environ.get("API_KEY", "")
        city = request.query_params.get("q")

        if not city:
            return Response({"error": "City is required"}, status=400)

        daily_forecasts = self.fetch_forecast(city, api_key)

        if daily_forecasts and daily_forecasts.is_valid():
            return Response(daily_forecasts.data, status=200)

        return Response({"error": "Invalid response from weather API"}, status=500)

    def fetch_forecast(self, city, api_key):
        response = requests.get(FORECAST_WEATHER_URL.format(city, api_key))
        return ForecastResponseSerializer(data=response.json())
