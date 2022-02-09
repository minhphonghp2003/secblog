from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('register/',views.register, name = "register"),
    path('',auth_view.LoginView.as_view(template_name='user/login.html'),name = 'login'),
    path('logout',auth_view.LogoutView.as_view(template_name='user/logout.html'),name = 'logout'),
]
