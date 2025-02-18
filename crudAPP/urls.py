from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers , name='crudhome'),
    path('<str:pk>', views.getUser, name='cruduser'),
    path('create', views.createUser, name='crudcreate'),
    path('update/<str:pk>', views.updateUser, name='crudupdate'),
    path('delete/<str:pk>', views.deleteUser, name='cruddelete'),
]