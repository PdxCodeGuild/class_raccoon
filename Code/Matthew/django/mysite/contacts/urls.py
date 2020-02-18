

from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('savecontact/', views.savecontact, name='savecontact'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
    path('delete/<int:contact_id>/', views.delete, name='delete'),
]


