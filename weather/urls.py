from django.urls import path
from . import views, views_forecast
from rest_framework.routers import DefaultRouter
from .views_forecast import WeatherViewSet

urlpatterns = [
    path("", views.weather, name="current_weather"),
    # path('/forecast', views_forecast.weather, name='forecast_weather'),
]

router = DefaultRouter()
router.register(r"forecast", WeatherViewSet, basename="forecast")

urlpatterns += router.urls