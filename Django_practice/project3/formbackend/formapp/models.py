from django.db import models
# Create your models here.

class user(models.Model):
    Name = models.CharField(max_length=250,blank=True,null=True)
    Email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=250,blank=True,null=True)
    
    # def __str__(self):
        # return f'{self.user.username}'
  


