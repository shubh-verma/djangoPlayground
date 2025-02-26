from django.urls import path
from weather import views

# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path(r"current", views.weather, name="current_weather"),
    path(r"forecast", views.ForecastAPIView.as_view(), name="forecast_weather"),
]

# router = DefaultRouter()
# router.register(r"forecast", WeatherViewSet, basename="forecast")

# urlpatterns += router.urls
