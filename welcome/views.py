from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'welcome/index.html')

def about(request):
    return render(request,'welcome/about.html')

def whoami(request):
    return render(request,'welcome/whoami.html')
