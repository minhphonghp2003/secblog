from django.contrib import admin
from django.urls import path, include


from .views import *
from . import views
urlpatterns = [
    path('', views.writeup_hpage,name = "wuhpage"),
    path('writeup/', Writeuplist.as_view(template_name ='writeup/writeup.html'), name="writeup"),
    path('writeup/<int:pk>/', WriteupDetail.as_view(template_name ='writeup/writeup_detail.html'), name="writeupdetail"),
    path('writeup/<str:username>/', UserWriteuplist.as_view(template_name ='writeup/userwriteup.html'), name="userwu"),
    path('more/<str:username>/', MyWriteuplist.as_view(template_name ='writeup/mywriteup.html'), name="mywu"),
]