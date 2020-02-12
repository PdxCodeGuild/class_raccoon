from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
  path('', views.index, name='index'),
  path('new_url/', views.new_url, name="new"),
  path('<str:shortform>/', views.redirect, name='redirect'),
]