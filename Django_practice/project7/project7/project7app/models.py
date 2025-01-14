from django.db import models

# Create your models here.
class Registration(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    photo = models.ImageField(upload_to='photo/',blank=True,null=True)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)

class Registration2(models.Model):
    fname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)