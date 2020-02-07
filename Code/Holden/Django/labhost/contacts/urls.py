from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('new/', views.new_contact, name='new_contact'),
    path('<int:contact_id>/edit/', views.edit_contact, name='edit_contact'),
    path('new/submit/', views.write_new_contact, name='write_new_contact'),
    path('<int:contact_id>/edit/submit/', views.write_edit_contact, name='write_edit_contact'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
