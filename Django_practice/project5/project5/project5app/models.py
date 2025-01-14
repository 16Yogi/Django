from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Project5(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Registration(models.Model):
    email = models.ForeignKey(User,max_length=250,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    dob = models.DateField(max_length=250)
    city = models.CharField(max_length=50)
    password1 = models.CharField(max_length=250)