from django.urls import path, include
from . import views 
app_name = 'contactslab'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('delete/<int:contactid>/', views.delete, name='delete'),

]
