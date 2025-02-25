
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import os
import requests
from .serializers import ForecastResponseSerializer

FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"


class WeatherViewSet(ViewSet):
    def list(self, request):
        return self.forecast(request)

    def create(self, request):
        return self.forecast(request)

    @action(detail=False, methods=["GET", "POST"])
    def forecast(self, request):
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
