from django.urls import path
from . import views

app_name = 'urlshort'

urlpatterns = [
  path('', views.index, name='index'),
  path('saveurl/', views.saveurl, name='saveurl'),
  path('sendit/<str:stub>', views.sendit, name='sendit'),
]