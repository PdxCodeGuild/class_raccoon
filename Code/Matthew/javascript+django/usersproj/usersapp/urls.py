
from django.urls import path
from . import views

app_name = 'usersapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register, name='register'),
  path('protected/', views.protected, name='protected'),
  path('register_user/', views.register_user, name='register_user'),
  path('logout/', views.logout, name='logout'),
  path('login/', views.login, name='login'),
]