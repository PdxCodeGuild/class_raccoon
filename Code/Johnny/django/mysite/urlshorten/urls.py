from django.urls import path
from . import views

app_name = 'urlshorten'
urlpatterns = [
    path('', views.index, name='index'),
    path('createurl/', views.createurl, name='createurl'),
    path('visit/<str:code>', views.visit, name='visit') #str:CODE is whatever var you want to assign to it
]
