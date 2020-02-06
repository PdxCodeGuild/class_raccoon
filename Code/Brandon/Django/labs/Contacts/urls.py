from django.urls import path

from . import views

app_name = 'Contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_view', views.contact_view, name='contact_view'),
    path('new_contact', views.new_contact, name='new_contact'),
    path('edit_contact', views.edit_contact, name='edit_contact'),
    path('delete_contact', views.delete_contact, name='delete_contact'),
    path('documentation', views.documentation, name='documentation')

]