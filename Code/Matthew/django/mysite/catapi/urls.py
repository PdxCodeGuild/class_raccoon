

from django.urls import path
from . import views

app_name = 'catapi'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cat_image_id>/', views.detail, name='detail'),
    path('favorite/<int:cat_image_id>/', views.favorite, name='favorite'),
    path('favorited/', views.favorited, name='favorited'),
    path('index2/', views.index2, name='index2')
]