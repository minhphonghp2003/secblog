from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    about_title = models.CharField(max_length=100)
    about_bio = models.TextField()
    about_phone = models.CharField(max_length=12, null=True)
    about_email = models.EmailField(null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    background = models.ImageField(default='defaultback.jpg',upload_to='profile_pics')
    about_ins = models.CharField(max_length=200, null=True)
    about_fb = models.CharField(max_length=200, null=True)
    about_zl = models.CharField(max_length=200, null=True)

    # education = models.ManyToManyField('Education' ,related_name="profile")
    # skill = models.ManyToManyField('Skill' ,related_name="profile")
    # experience = models.ManyToManyField('Experience' ,related_name="profile")
   
    def __str__(self):
        return self.user.username + "'s profile" 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 500 or img.width > 500 or img.width < 500:
            out_size =(500,500)
            img.thumbnail(out_size)
            img.save(self.image.path)
        
        



class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="edu")

    edu_title = models.CharField(max_length=100, null=True)
    edu_year = models.DateField( null=True)
    edu_schoolname = models.CharField(max_length=100, null=True)
    edu_address = models.CharField(max_length=100, null=True)
    edu_content = models.TextField( null=True)

    def __str__(self):
        return self.edu_title + "'s education" 
    def get_absolute_url(self):
        return reverse('profupdate') 

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="skill")

    skill_title = models.CharField(max_length=100, null=True)
    skill_progress = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    def __str__(self):
        return self.skill_title + "'s skill" 
    def get_absolute_url(self):
        return reverse('profupdate')

class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="exp")

    exp_title = models.CharField(max_length=100, null=True)
    exp_year  = models.DateField(null=True)
    exp_descript = models.TextField(null=True)
    
    def __str__(self):
        return self.exp_title + "'s exps" 
    def get_absolute_url(self):
        return reverse('profupdate')



