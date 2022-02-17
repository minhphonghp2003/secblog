from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',views.register, name = "register"),
    path('',auth_view.LoginView.as_view(template_name='user/login.html'),name = 'login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name = 'logout'),
    path('passwdreset/',auth_view.PasswordResetView.as_view(template_name='user/passwdreset.html'),name = 'passwdreset'),
    path('passwdresetdone/',auth_view.PasswordResetDoneView.as_view(template_name='user/passwdresetdone.html'),name = 'password_reset_done'), 
    path('passresetconfirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='user/passwdresetconfirm.html'),name = 'password_reset_confirm'),
    path('passwdresetcompleted/',auth_view.PasswordResetCompleteView.as_view(template_name='user/passwdresetcompleted.html'),name = 'password_reset_complete'),

    
    

]   

  
