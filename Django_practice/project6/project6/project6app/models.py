from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class MovieListForm(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    movieName = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RegistrationForm(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
