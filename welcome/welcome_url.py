from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.home,name = "welcomehome"),
    path('about/',views.about,name = "wel_about"),
    path('whoami/',views.whoami,name = "whoami"),
    path('success/',views.Success,name= 'success'),
]