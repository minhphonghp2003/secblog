from django.shortcuts import render, redirect
from django.contrib import messages
from .form import Register
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('first_name')
            usrname=form.cleaned_data.get('username')
            
            messages.success(request,f"Account created for '{name}'. Now you can login as '{usrname}'")
            return redirect('login')
       
            
    else:
        form = Register()
    
    return render(request, 'user/register.html/',{'form':form})


@login_required
def profile(request):
    context = {
        
        'education' : Education.objects.all(),
        'skills' : Skill.objects.all(),
        'experience' : Experience.objects.all(),
    }
    return render(request,'user/profile.html/',context)