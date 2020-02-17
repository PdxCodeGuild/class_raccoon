from django.urls import path
from . import views

app_name = 'lab4app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
]