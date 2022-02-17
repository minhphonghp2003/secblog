import re
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .form import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('first_name')
            usrname=form.cleaned_data.get('username')
            
            messages.success(request,f"Account created for '{name}', now you can login as '{usrname}'. You should update your profile")
            return redirect('login')
       
            
    else:
        form = Register()
    
    return render(request, 'user/register.html/',{'form':form})



def profile(request, p):
   
    if request.method == 'POST':
        name = request.POST.get('name')
        subject =  request.POST.get('subject')
        
        fromemail = request.POST.get('email')
        message = 'Sent from: '+ fromemail + ' ( '+ name+ ' )' + '\n'+'Subject: '+ subject + '\n' + "Message: " + str(request.POST.get('message'))
        toemail = request.POST.get('toemail')
        messages.success(request,"Email sent")
        try:
            send_mail('Email sent from visitor at secblog.', message, fromemail, [toemail])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
        
    
    context = {
    'profile' : Profile.objects.filter(user=p).first(),
    'username' : User.objects.filter(id=p).first(),
    }
    return render(request,'user/profile.html/',context)
    

class Eduupdate(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    
    model = Education
    template_name = 'user/edu.html'
    
    form_class = EducationUpdate

    success_message= "Your education information has been updated"

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

class Skillupdate(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    
    model = Skill
    template_name = 'user/skill.html'
    success_message= "Your skills information has been updated"
    form_class = SkillUpdate

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

class Expupdate(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    
    model = Experience
    template_name = 'user/exp.html'
    success_message= "Your Exprience information has been updated"
    form_class = ExperienceUpdate
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

class EduCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Education
    template_name = 'user/edu.html'
    
    form_class = EducationUpdate

    success_message= "Your education information has been created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
class SkillCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Skill
    template_name = 'user/skill.html'
    
    form_class = SkillUpdate

    success_message= "Your Skills information has been created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
class ExpCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Experience
    template_name = 'user/exp.html'
    
    form_class = ExperienceUpdate

    success_message= "Your experience information has been created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class Edudel(UserPassesTestMixin,SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Education
    success_url = '/profile/myprofile/update'
    template_name ='user/edudel.html'
    success_message= "Your education information has been deleted"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False
    

class Skilldel(UserPassesTestMixin,SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Skill
    success_url = '/profile/myprofile/update'
    template_name ='user/skilldel.html'
    success_message= "Your skill information has been delete"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False


class Expdel(UserPassesTestMixin,SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Experience
    success_url = '/profile/myprofile/update'
    template_name ='user/expdel.html'
    success_message= "Your experience information has been delete"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

@login_required
def profileupdate(request):
    profile = get_object_or_404(Profile,user=request.user)
    if request.method == 'POST':
        
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate( request.POST,request.FILES, instance=profile)
        
       
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            profile_id = request.user.id
            messages.success(request,"Your profile has been updated!")
            return redirect('profile',p=profile_id)
         
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate( instance=request.user.profile)   
    context = {
        'u_form': u_form,
        'p_form': p_form   
    }
    return render(request,'user/profileupdate.html', context )