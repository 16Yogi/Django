from django import forms 
# from .models import Project5 
# from .models import Registration
from .models import * 

class Project5Form(forms.ModelForm):
    class Meta:
        model = Project5 
        fields = ['text','photo']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration 
        fields = ['email','fullname','dob','password1']