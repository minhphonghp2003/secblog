from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Cate(models.Model):
    
    image= models.ImageField(default='defaultback.jpg',upload_to = 'cate')
    tag = models.CharField(default='challenge',max_length=100)
    def __str__(self):
        return self.tag

class Writeup(models.Model):
    
    like = models.ManyToManyField(User,related_name='like',null=True,blank=True)
    title = models.TextField()
    prerequis =  RichTextUploadingField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    cate = models.ManyToManyField(Cate, related_name='writeup')
    date_create = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='writeup')



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writeupdetail',kwargs={'pk':self.pk} ) 

class Commment(models.Model):
    writeup = models.ForeignKey(Writeup, on_delete=models.CASCADE, related_name='cmt')
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cmt',null=True)
    def __str__(self):
        return 'writeup={0}'.format(self.writeup)