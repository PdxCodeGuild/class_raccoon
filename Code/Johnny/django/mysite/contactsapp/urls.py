from django.urls import path
from . import views

app_name = 'contactsapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('delete/<int:contact_id>/', views.delete, name='delete'),
  path('<int:contact_id>/edit/', views.edit, name='edit')
]
