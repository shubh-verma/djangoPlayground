from django.urls import path
from . import views

# from rest_framework.routers import DefaultRouter
from .views import WeatherAPIView

urlpatterns = [
    path("current", views.weather, name="current_weather"),
    path("forecast/", WeatherAPIView.as_view(), name="forecast_weather"),
]

# router = DefaultRouter()
# router.register(r"forecast", WeatherViewSet, basename="forecast")

# urlpatterns += router.urls
