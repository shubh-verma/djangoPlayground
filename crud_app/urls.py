from django.urls import path
from crud_app import views

urlpatterns = [
    path(r"", views.getUsers, name="crudhome"),
    path(r"<str:pk>", views.getUser, name="cruduser"),
    path(r"create", views.createUser, name="crudcreate"),
    path(r"update/<str:pk>", views.updateUser, name="crudupdate"),
    path(r"delete/<str:pk>", views.deleteUser, name="cruddelete"),
]
