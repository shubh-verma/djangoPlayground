from django.urls import path
from . import views

urlpatterns = [
    path('/', views.getUsers , name='home'),
]