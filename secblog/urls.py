"""secblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as userview
from user.views import *
urlpatterns = [
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
    path('',include('welcome.welcome_url')),
    path('user/',include('user.user_url')),
    path('dedsec/',include('writeup.writeup_url')),

    path('profile/<str:p>/',userview.profile, name = "profile"),
    path('profile/myprofile/update/',userview.profileupdate, name = "profupdate"),

    path('profile/myedu/<str:pk>/',Eduupdate.as_view(), name = "eduupdate"),
    path('profile/myskill/<str:pk>/',Skillupdate.as_view(), name = "skillupdate"),
    path('profile/myexp/<str:pk>/',Expupdate.as_view(), name = "expupdate"),

    path('profile/newedu', EduCreate.as_view(), name="educreate"),
    path('profile/newskill', SkillCreate.as_view(), name="skillcreate"),
    path('profile/newexp', ExpCreate.as_view(), name="expcreate"),

    path('profile/deledu/<str:pk>/',Edudel.as_view(), name = "edudelete"),
    path('profile/delskill/<str:pk>/',Skilldel.as_view(), name = "skilldelete"),
    path('profile/delexp/<str:pk>/',Expdel.as_view(), name = "expdelete"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
