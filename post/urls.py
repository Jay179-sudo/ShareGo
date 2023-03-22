from django.contrib import admin
from django.urls import path
from .views import home, upload_file, content, detailcontent

urlpatterns = [
    path('', home, name='home'),
    path('content', content, name='content'),
    path('upload', upload_file, name='upload'),
    path('content/detail/<str:username>', detailcontent, name='detail')
    
]