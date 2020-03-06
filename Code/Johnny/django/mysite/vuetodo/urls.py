from django.urls import path
from . import views

app_name = 'vuetodo'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('create_post/', views.create_post, name='create_post')
]
