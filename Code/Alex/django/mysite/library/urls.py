from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
  path('index/', views.index, name='index')
]