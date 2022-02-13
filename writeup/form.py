from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Writeupform(forms.ModelForm):
    class Meta:
        model = Writeup
        field = '__all__'
        exclude = ['author','date_create']