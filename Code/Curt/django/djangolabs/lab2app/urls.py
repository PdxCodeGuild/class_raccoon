from django.urls import path
from . import views

app_name = 'lab2app'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<int:contact_item_id>/', views.contact_id, name='contact_id'),
    path('contacts/new/', views.new_contact, name='new_contact'),
    path('contacts/<int:contact_item_id>/edit/', views.edit_contact, name='edit_contact'),
    path('contacts/update/<int:contact_item_id>/', views.update_contact, name='update_contact'),
    path('contacts/new/', views.new_contact, name='new_contact'),
    path('contacts/delete/<int:contact_item_id>/', views.delete_contact, name='delete_contact'),
]