from django.urls import path

from pokemon_EV_auto_calculation import views


urlpatterns = [
    path("", views.input, name="input"),
    path("input/", views.input, name="input"),
    path("result/", views.result, name="result"),
]

