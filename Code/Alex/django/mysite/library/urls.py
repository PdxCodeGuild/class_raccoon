from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('checkout/', views.checked_out, name='checked_out'),
  path('detail/<int:book_id>/', views.detail, name='detail'),
  path('checked_in/<int:book_id>/', views.checked_in, name='checked_in')
]