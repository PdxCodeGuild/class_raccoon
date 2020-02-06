
from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('completetodo/', views.completetodo, name='completetodo'),
    path('deletetodo/<todo_item_id>/', views.deletetodo, name='deletetodo'),
]
