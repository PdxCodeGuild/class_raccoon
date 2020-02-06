
from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('api/', views.api, name='api'),
    path('<str:path>/', views.other, name='other'),
]



