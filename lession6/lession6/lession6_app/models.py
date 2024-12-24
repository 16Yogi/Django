from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class lession6(models.Model):
    LESSION_CHOICE = [
        ('lession1','1'),
        ('lession2','2'),
        ('lession3','3'),
        ('lession4','4'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lession/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10,choices=LESSION_CHOICE)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    


# One to Many 
class lessionReview(models.Model):
    lession = models.ForeignKey(lession6, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.lession.name}'
    

# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    lession_list = models.ManyToManyField(lession6,related_name='lessions')

    def __str__(self):
        return self.name
    
# one to one
class lessionCertificate(models.Model):
    lession = models.OneToOneField(lession6,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.lession}'


