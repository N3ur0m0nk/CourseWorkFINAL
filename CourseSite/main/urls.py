from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.get_name, name="index"),
path("<str:id>/", views.index, name="index"),
]
