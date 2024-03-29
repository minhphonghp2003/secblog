from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Register(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1', 'password2']


class UserUpdate(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['first_name','last_name']

class ProfileUpdate(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields='__all__'
        exclude = ['user','tag']

class EducationUpdate(forms.ModelForm):
    
    class Meta:
        model=Education
        fields='__all__'
        exclude = ['user']

class SkillUpdate(forms.ModelForm):
    
    class Meta:
        model=Skill
        fields='__all__'
        exclude = ['user']

class ExperienceUpdate(forms.ModelForm):
    
    class Meta:
        model=Experience
        fields='__all__'
        exclude = ['user']