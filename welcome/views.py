from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError

from django.conf import settings
# Create your views here.
def home(request):
    

    return render(request,'welcome/index.html')

def about(request):
    return render(request,'welcome/about.html')

def whoami(request):
    return render(request,'welcome/whoami.html')

def Success(request):
    if request.method == 'POST':
       
        name =request.POST.get('name')
        subject = 'From ' + name
        from_email = request.POST.get('email')
        
        message ='Email from: ' + from_email+' (' + name +')' + '\n'+'Message: '+  request.POST.get('message') + '\n'
        try:
            send_mail(subject, message, from_email, ['minhphonghp2003@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return JsonResponse({'date':'null',})
    