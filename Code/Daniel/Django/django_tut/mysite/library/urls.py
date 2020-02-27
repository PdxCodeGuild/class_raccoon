from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('checkout/<int:bookid>/', views.checkout, name='checkout'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('checkin/<int:bookid>/', views.checkin, name='checkin'),
    path('bookinfo/<int:bookid>/', views.bookinfo, name='bookinfo')   
]
