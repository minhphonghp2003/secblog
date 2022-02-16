from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .form import *
# from django.core import serializers
from user.models import Profile
from .models import Writeup
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
def writeup_hpage(request):
    context = {
        'writeup' : Writeup.objects.all().order_by("-date_create"),
        'profile' : Profile.objects.all(),
        'contrib' :Profile.objects.filter(tag= 'contributor').count, 
        'cate' : Cate.objects.all().count
    }
    return render(request,'writeup/index.html',context)
    
def about(request):
    return render(request,'writeup/about.html')
class Writeuplist(ListView):
    model = Writeup
    context_object_name = 'post'
    paginate_by = 9
    def get_queryset(self) :
        
        return Writeup.objects.all().order_by('-date_create')
    

class UserWriteuplist(ListView):
    model = Writeup
    context_object_name = 'post'
    paginate_by = 9
    def get_queryset(self) :
        user = get_object_or_404(User,username=self.kwargs.get('username'))

        return Writeup.objects.filter(author=user).order_by('-date_create')
    
    

class WriteupDetail(DetailView):
    model = Writeup
    context_object_name = 'post'

class WriteupCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Writeup
    form_class= Writeupform
    template_name = 'writeup/writeup_create.html'
    success_message= "Writeup created"

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)


class WriteupDelete(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,DeleteView):
    model = Writeup
    success_url = '/dedsec/writeup'
    template_name ='writeup/writeup_delete.html'
    success_message= "Writeup deleted"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class WriteupUpdate(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    
    model = Writeup
    template_name = 'writeup/writeup_create.html'
    success_message= "Writeup updated"
    form_class = Writeupform
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class CateList(ListView):
    model = Cate
    template_name = 'cate/cate.html'
    context_object_name = 'cates'

class CateDetail(ListView):
    model = Writeup
    template_name = 'cate/catedetail.html'
    context_object_name = 'posts'
    def get_queryset(self) :
        t = get_object_or_404(Cate,tag=self.kwargs.get('tag'))
        return Writeup.objects.filter(cate=t).order_by('-date_create')


@login_required
def Like(request):
    if request.POST.get('action') == 'post' :
        result = 0
        id = int(request.POST.get('postid'))
        writeup = get_object_or_404(Writeup,id = id)
        if writeup.like.filter(id=request.user.id).exists():
            writeup.like.remove(request.user)
            result = -1
            
        else:        
            writeup.like.add(request.user)
            result =1
       
        return JsonResponse({'result':result,})

def Cmt(request):
    if request.method == "POST":
        if request.POST.get('content'):
            id = request.POST.get('wu_id')
            writeup = get_object_or_404(Writeup,id=id)
            content = request.POST.get('content')
            user = request.user
            
            
            writeup.cmt.create(user=user,content=content)
           
            return JsonResponse({'message':'Your comment created',})

    return JsonResponse({'content':'null'})

def CmtDel(request):
    if request.method == 'POST':
        id = request.POST.get('cmtid')
        cmt = get_object_or_404(Commment, id=id)
        cmt.delete()
        data = {
            'message' : 'Comment deleted',

        }
        return JsonResponse(data)
    
    return JsonResponse({'data':'null'})