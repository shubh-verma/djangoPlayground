# Create your views here.

from rest_framework import status
from weather.serializers import WeatherSerializer, ForecastResponseSerializer
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.views.decorators.cache import cache_page
from storefront.settings import api_key

FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


@cache_page(60 * 1)
@api_view(["GET", "POST"])
def weather(request):

    city = request.query_params.get("q")

    if not city:
        return Response(
            {"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    current_weather = fetch_weather(city, api_key)

    if current_weather and current_weather.is_valid():
        return Response(current_weather.data, status=status.HTTP_200_OK)

    return Response(
        {"error": "Invalid response from weather API"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def fetch_weather(city, api_key):
    weather_response = requests.get(CURRENT_WEATHER_URL.format(city, api_key))
    return WeatherSerializer(data=weather_response.json())


class ForecastAPIView(APIView):
    @method_decorator(cache_page(60 * 1 * 1), name="dispatch")
    def get(self, request, format=None):
        city = request.query_params.get("q")

        if not city:
            return Response(
                {"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        daily_forecasts = self.fetch_forecast(city, api_key)

        if daily_forecasts and daily_forecasts.is_valid():
            return Response(daily_forecasts.data, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid response from weather API"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def fetch_forecast(self, city, api_key):
        response = requests.get(FORECAST_WEATHER_URL.format(city, api_key))
        return ForecastResponseSerializer(data=response.json())
