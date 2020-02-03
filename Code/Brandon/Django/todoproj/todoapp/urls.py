from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('savetodo/', views.savetodo, name='savetodo')
]