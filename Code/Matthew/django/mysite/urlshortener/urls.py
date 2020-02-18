

from django.urls import path
from . import views

app_name = 'urlshortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
    path('<int:urlredirect_id>/', views.detail, name='detail'),
    path('<str:code>/', views.redirect, name='redirect')
]
