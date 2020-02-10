from django.urls import path
from . import views

app_name = 'urlshortener'
urlpatterns = [
  path('index/', views.index, name='index')
]