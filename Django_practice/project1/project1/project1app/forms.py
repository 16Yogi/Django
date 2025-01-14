from django import forms  
from .models import Project #this is models class name
from django.contrib.auth.forms import UserCreationForm #registaion
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['text','photo'] 

# registation
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    