from django.urls import path
from . import views

app_name = 'urlshorten'
urlpatterns = [
    path('', views.index, name='index')
]
