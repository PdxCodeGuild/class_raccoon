

from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
  path('', views.index, name='index'),
  path('suggestions/', views.suggestions, name='suggestions'),
  path('increment_counter/', views.increment_counter, name='increment_counter')
]