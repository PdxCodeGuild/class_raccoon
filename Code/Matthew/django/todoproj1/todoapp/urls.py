

from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_todo/', views.savetodo, name='savetodo'),
    path('about/', views.about, name='about'),
]
