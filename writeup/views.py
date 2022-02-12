from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from user.models import Profile
from .models import Writeup
from django.contrib.auth.models import User
 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def writeup_hpage(request):
    return render(request,'writeup/index.html')
    
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
    
    

class WriteupDetail(DeleteView):
    model = Writeup
    context_object_name = 'post'
