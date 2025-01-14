from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = Registration
#         fields = ('fullname','email','photo','country','state','city','password1')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('fullname', 'email', 'photo', 'country', 'state', 'city', 'password1') 
        widgets = {
            'password1': forms.PasswordInput(), 
        }