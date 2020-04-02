

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
  path('', views.index, name='index'),
  path('login_register/', views.login_register, name='login_register'),
  path('public/', views.public, name='public'),
  path('protected/', views.protected, name='protected'),
  path('login/', views.login, name='login'),
  path('register/', views.register, name='register'),
  path('logout/', views.logout, name='logout')
]
