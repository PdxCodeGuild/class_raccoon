from django.urls import path

from . import views

app_name = 'urlshortener'

urlpatterns = [
    # index view
    path('', views.index, name='index'),
    # create view that redirects to index page after saving
    path('create/', views.create, name='create'),
    # passes the short url to the visit page that will pull the site byusing the short url then render the page to the full url
    path('<str:short_url>/', views.visit, name='visit'),
    # Sends to the delete view that will redirect to the index page updated
    path('delete/<int:url_id>/', views.delete, name='delete'),
]