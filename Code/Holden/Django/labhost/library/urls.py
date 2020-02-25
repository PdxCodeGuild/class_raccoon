from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('usercheckouts/', views.user_checkouts, name='user_checkouts'),
    path('book/<int:book_id>', views.book_view, name='book_view'),
    path('checkout/<int:book_id>', views.book_checkout, name='book_checkout'),
    path('checkin/<int:checkout_id>', views.checkin, name='checkin'),
]