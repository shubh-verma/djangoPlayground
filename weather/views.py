# Create your views here.

from rest_framework import status
from weather.serializers import WeatherSerializer, ForecastResponseSerializer
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.views.decorators.cache import cache_page
from django.conf import settings

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, authentication_classes

FORECAST_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


@cache_page(60 * 1)
@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def weather(request):

    city = request.query_params.get("q")

    if not city:
        return Response(
            {"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    current_weather = fetch_weather(city)

    if current_weather and current_weather.is_valid():
        return Response(current_weather.data, status=status.HTTP_200_OK)

    return Response(
        {"error": "Invalid response from weather API"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def fetch_weather(city):
    weather_response = requests.get(CURRENT_WEATHER_URL.format(city, settings.API_KEY))
    return WeatherSerializer(data=weather_response.json())


class ForecastAPIView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 1 * 1), name="dispatch")
    def get(self, request):
        city = request.query_params.get("q")

        if not city:
            return Response(
                {"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        daily_forecasts = self.fetch_forecast(city)

        if daily_forecasts and daily_forecasts.is_valid():
            return Response(daily_forecasts.data, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid response from weather API"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def fetch_forecast(self, city):
        response = requests.get(FORECAST_WEATHER_URL.format(city, settings.API_KEY))
        return ForecastResponseSerializer(data=response.json())
