

from django.urls import path
from . import views


app_name = 'usersajax'
urlpatterns = [
  path('', views.index, name='index'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('get_user_data/', views.get_user_data, name='get_user_data')
]



