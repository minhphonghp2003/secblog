from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.contrib import messages
from .form import *
from .models import *
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
   
    context = {
        'profile' : Profile.objects.filter(user=p).first(),
        'username' : User.objects.filter(id=p).first(),

        
    }
    return render(request,'user/profile.html/',context)


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