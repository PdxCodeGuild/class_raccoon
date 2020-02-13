from django.urls import path
from . import views

app_name = "rpsgame"

urlpatterns = [
    path("", views.index, name="index"),
    path("play/", views.play, name="play"),
    path("scores/", views.score, name="scores"),
]