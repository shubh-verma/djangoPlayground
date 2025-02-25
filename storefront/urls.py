from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("playground/", include("playground.urls")),
    path("users/", include("crudAPP.urls")),
    path("openWeather/", include("openWeather.urls")),  # Debug toolbar URLS
    path("weather/", include("weather.urls")),  # Debug toolbar URLS
] + debug_toolbar_urls()
