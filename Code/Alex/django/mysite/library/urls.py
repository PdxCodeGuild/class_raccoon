from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('checkout/', views.checked_out_or_not, name='checked_out_or_not')
]