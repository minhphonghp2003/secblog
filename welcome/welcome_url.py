from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home,name = "welcomehome"),
    path('about/',views.about,name = "wel_about"),
    path('whoami/',views.whoami,name = "whoami"),
    path('success/',views.Success,name= 'success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)