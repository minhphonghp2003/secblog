from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class MailF(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    
    message = forms.CharField(widget=forms.Textarea, required=True)