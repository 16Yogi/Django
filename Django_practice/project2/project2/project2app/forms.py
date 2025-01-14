from django import forms 
from .models import Project2  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User 

class ProjectForm(UserCreationForm):
    class Meta:
        model = Project2
        fields = ['text','photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User   
        fields = ('username','email','password1','password2')