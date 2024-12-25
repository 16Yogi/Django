from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class lessions(models.Model):
    LESSON_CHOICES = [
        ('lesson1', '1'),
        ('lesson2', '2'),
        ('lesson3', '3'),
        ('lesson4', '4'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lession/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=LESSON_CHOICES)
    description = models.TextField(max_length=250, default='No description available')  # Provide a default value

    def __str__(self):
        return self.name
