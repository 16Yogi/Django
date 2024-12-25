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

# one to many
class lessionReview(models.Model):
    lession = models.ForeignKey(lessions,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.lession.name}'

# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lession_list = models.ManyToManyField(lessions,related_name='lessionos')

    def __str__(self):
        return self.name 

# one to one
class lessionCertificate(models.Model):
    lession = models.OneToOneField(lessions,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.lession}'