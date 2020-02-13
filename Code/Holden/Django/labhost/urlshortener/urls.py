from django.urls import path

from . import views

app_name = 'urlshortener'
urlpatterns = [
    path('', views.blankredir, name='blank'),
    path('index/', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('<str:short_code>/', views.shortened, name='shortened')
]
