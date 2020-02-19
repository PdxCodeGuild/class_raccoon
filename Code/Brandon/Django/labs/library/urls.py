from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('view/', views.view, name='view'),
    path('checkout/<int:book_id>/', views.check_out, name='checkout')

]
