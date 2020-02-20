from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
  path('', views.index, name='index'),
  path('by_title', views.title, name='title'),
  path('by_author', views.author, name='author'),
  path('author_details/<str:name>/', views.author_details, name='author_details'),
  path('book_details/<int:book_id>/', views.book_details, name='book_details'),
  path('checkout/<int:book_id>/', views.checkout, name='checkout'),
  path('user', views.user_details, name='user_details'),
  path('checkin', views.checkin, name='checkin'),
]