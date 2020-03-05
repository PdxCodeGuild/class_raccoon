from django.urls import path
from . import views

app_name = 'vuetodo'
urlpatterns = [
    path('', views.index, name='index')
]
