from django.urls import path
from . import views

app_name = 'contactsapp'

urlpatterns = [
  path('', views.index, name='index'),
  path('savecontact/', views.savecontact, name='savecontact'),
  path('deletecontact/<int:contact_id>/', views.deletecontact, name='deletecontact'),
]
