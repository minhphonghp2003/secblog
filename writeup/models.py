from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

class Cate(models.Model):
    
    
    tag = models.CharField(default='challenge',max_length=100)
    def __str__(self):
        return self.tag

class Writeup(models.Model):
    

    title = models.CharField(max_length=100)
    prerequis = models.TextField()
    content = models.TextField()
    cate = models.ManyToManyField(Cate, related_name='writeup')
    date_create = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='writeup')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writeupdetail',kwargs={'pk':self.pk} ) 

