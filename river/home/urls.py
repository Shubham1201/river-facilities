from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.home, name='home'),
    path('ytdownload/', views.ytdownload, name='ytdownload'),
    path('ytdownload/download/', views.download, name='download'),
    # path('ytdownload/download/<res>', views.download_complete, name='download_complete'),
    path('youtubetags/', views.youtubetags, name='youtubetags'),
    path('youtubetags/youtubetagsget/', views.tagsget, name='tagsget'),
]