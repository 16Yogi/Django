from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User 

class TestForm(forms.Form):
    fullname = forms.CharField(label='Your name',max_length=250)
    email = forms.CharField(label='Email',max_length=250)

class MovieUpload(forms.ModelForm):
    class Meta:
        model = MovieListForm
        fields = ['movieName','photo']

class UserRegistration(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
    )
    class Meta:
        model = RegistrationForm
        fields = ['fullname','email','dob','country','state','city','password1','password2']




