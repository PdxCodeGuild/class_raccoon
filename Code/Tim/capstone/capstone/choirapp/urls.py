from django.urls import path
from . import views

app_name = 'choirapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('infolder/', views.in_folder, name='in_folder'),
    path('turnin/', views.turn_in, name='turn_in'),
    path('thisseason/', views.this_season, name='this_season'),
    path('lib_login/', views.lib_login, name='lib_login'),
    path('save_piece/', views.save_piece, name='save_piece'),
    path('edit_due/', views.edit_due, name='edit_due'),
    path('rehearsal/', views.rehearsal, name='rehearsal'),
    path('schedule/', views.schedule, name='schedule'),
    path('set_folder', views.set_folder, name='set_folder')
    ]
