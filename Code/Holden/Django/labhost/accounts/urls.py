from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.user_home, name='home'),
    path('login/', views.login_page, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('save_user/', views.save_user, name='save_user'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
]
