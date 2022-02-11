from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    about_title = models.CharField(max_length=100)
    about_bio = models.TextField()
    about_phone = models.CharField(max_length=12, null=True)
    about_email = models.EmailField(null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    about_ins = models.CharField(max_length=200, null=True)
    about_fb = models.CharField(max_length=200, null=True)
    about_zl = models.CharField(max_length=200, null=True)

   
    def __str__(self):
        return self.user.username + "'s profile" 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 150 or img.width > 150:
            out_size =(150,150)
            img.thumbnail(out_size)
            img.save(self.image.path)




class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    edu_title = models.CharField(max_length=100, null=True)
    edu_year = models.DateField( null=True)
    edu_schoolname = models.CharField(max_length=100, null=True)
    edu_address = models.CharField(max_length=100, null=True)
    edu_content = models.TextField( null=True)

    def __str__(self):
        return self.user.username + "'s education" 
    

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    skill_title = models.CharField(max_length=100, null=True)
    skill_progress = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    def __str__(self):
        return self.user.username + "'s skill" 

class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)   

    exp_title = models.CharField(max_length=100, null=True)
    exp_year  = models.DateField(null=True)
    exp_descript = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username + "'s exps" 