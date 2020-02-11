from django.urls import path

from . import views

app_name = 'shorts'

urlpatterns = [
    path('', views.index, name='index'),
]