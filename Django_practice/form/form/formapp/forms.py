from django import forms
from .models import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User  

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Form 
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']