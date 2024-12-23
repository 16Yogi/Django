from django.db import models
from django.utils import timezone

# Create your models here.

class lessions(models.Model):
    LESSION_CHOICES = [
        ('lession1','1'),
        ('lession2','2'),
        ('lession3','3'),
        ('lession4','4'),
    ]
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='lessions/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=8,choices=LESSION_CHOICES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    

    