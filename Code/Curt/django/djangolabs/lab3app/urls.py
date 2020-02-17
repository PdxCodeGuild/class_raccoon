from django.urls import path
from . import views

app_name = 'lab3app'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
]