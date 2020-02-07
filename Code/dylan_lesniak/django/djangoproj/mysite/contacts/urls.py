from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:contact_id>/', views.details, name='details'),
  path('<int:contact_id>/edit/', views.edit, name="edit"),
  path('<int:contact_id>/edit/save_edit/', views.save_edit, name="save_edit"),
  path('new_form/', views.new_form, name="new_form"),
  path('save_new/', views.save_new_form, name="save_new_form"),
  path('delete/<int:contact_id>/', views.delete, name="delete"),
]