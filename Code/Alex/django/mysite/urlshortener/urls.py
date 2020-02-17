from django.urls import path
from . import views

app_name = 'urlshortener'
urlpatterns = [
  path('', views.index, name='index'),
  path('saveurl/', views.saveurl, name='saveurl'),
  path('redirect/', views.redirect, name='redirect'),
]