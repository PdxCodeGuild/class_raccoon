from django.urls import path
from . import views

app_name = "res_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('restaurants/', views.get_restaurants, name="restaurants"),
    path('save_res/', views.save_reservation, name="save_res"),
    path('reservations/', views.reservations, name="reservations")
]