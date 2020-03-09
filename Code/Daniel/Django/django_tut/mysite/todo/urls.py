from django.urls import path
from . import views

app_name='todo'
urlpatterns=[
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
]