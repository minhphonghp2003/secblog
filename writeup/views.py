from django.shortcuts import render,get_object_or_404, redirect
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


class Contrib(ListView):
    model = User
    template_name = 'writeup/contrib.html'
    context_object_name = 'obj'
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super(Contrib, self).get_context_data(**kwargs)
        context['cont'] = Profile.objects.filter(tag='contributor')     
        return context



def Search(request):
    if request.method == "POST" :
        search = request.POST.get('search')        
        userf_n = []
        writeup = []
        cate = []
        context_in_wu = {}

        

        for u in User.objects.all():
            if search in u.first_name or search in u.last_name or search in u.username :
                userf_n.append(User.objects.filter(username = u.username).first())
        for w in Writeup.objects.all():
            if search in w.title :     
                writeup.append( Writeup.objects.filter(title=w.title).first())
            if w.content_upload and search in w.content_upload:
                context_in_wu.update({w:( w.content_upload[w.content_upload.index(search)+ len(search):w.content_upload.index(search) + len(search)+30])})
        for c in Cate.objects.all():
            if search in c.tag:
                cate.append( Cate.objects.filter(tag = c.tag).first())

        data = {
            'usrfn': userf_n,
            'search': search,
            'writeup': writeup,
            'cate' : cate,
            'context' : context_in_wu,
        }
        return render(request,'writeup/search.html',data)

    
    

        



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
           
            return JsonResponse({'message':'Your comment sent',})

    return JsonResponse({'content':'null'},status = 400)

def CmtDel(request):
    if request.method == 'POST':
        id = request.POST.get('cmtid')
        cmt = get_object_or_404(Commment, id=id)
        cmt.delete()
        data = {
            'message' : 'Comment deleted',

        }
        return JsonResponse(data)
    
    return JsonResponse({'data':'null'},status = 400)