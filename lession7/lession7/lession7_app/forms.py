from django import forms
from .models import lessions


class lessionVerityForm(forms.Form):
    lession_verity = forms.ModelChoiceField(queryset=lessions.objects.all(),label="Select lession variety")
    #  lession_verity = forms.CharField()
    