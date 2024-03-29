from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from . import views
urlpatterns = [
    path('', views.writeup_hpage,name = "wuhpage"),
    path('writeup/', Writeuplist.as_view(template_name ='writeup/writeup.html'), name="writeup"),
    path('writeup/<int:pk>/', WriteupDetail.as_view(template_name ='writeup/writeup_detail.html'), name="writeupdetail"),
    path('writeup/<str:username>/', UserWriteuplist.as_view(template_name ='writeup/userwriteup.html'), name="userwu"),
    path('writeupcreate/', WriteupCreate.as_view(), name="writeupcreate"),
    path('writeup/<int:pk>/delete', WriteupDelete.as_view(), name="writeupdelete"),
    path('writeup/<int:pk>/update', WriteupUpdate.as_view(), name="writeupupdate"),
    
    path('category/',CateList.as_view(),name = 'cate'),
    path('category/<str:tag>/', CateDetail.as_view(), name = 'catedetail'),

    
    path('like/',views.Like,name = 'like'),
    path('comment/',views.Cmt, name='cmt'),
    path('comment/delete',views.CmtDel, name = 'cmtdel'),

    path('contrib/',Contrib.as_view(), name = 'contrib'),

    path('search/',views.Search,name = 'search'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)