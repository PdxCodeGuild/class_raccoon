from django.urls import path

from . import views

app_name = 'Contacts'

urlpatterns = [
    # a list of all the contacts
    path('', views.index, name='index'),
    # show the user a page for editing a single contact
    path('contact_view/<int:contact_id>/', views.contact_view, name='contact_view'),
    path('new_contact/', views.new_contact, name='new_contact'),
    # receive form submission from contact_view page
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('documentation/', views.documentation, name='documentation')

]