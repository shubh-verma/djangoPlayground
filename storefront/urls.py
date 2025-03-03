from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"playground/", include("playground.urls")),
    path(r"users/", include("crud_app.urls")),  # Debug toolbar URLS
    path(r"weather/", include("weather.urls")),
    path(r'search/', include('opensearch_dvdrental.urls')),  # Debug toolbar URLS
] + debug_toolbar_urls()
