from django.urls import path

from . import views

app_name = 'shorts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:short_url>/', views.visit, name='visit'),
    path('delete/<int:url_id>/', views.delete, name='delete'),
]