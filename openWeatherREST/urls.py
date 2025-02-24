
from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_weather_REST, name='open_weather_REST'),
]