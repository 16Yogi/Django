from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import lessions

# Create your views here.

def app_index(request):
    lession = lessions.objects.all()
    return render(request, 'index_app.html', {'lession': lession})

def app_about(request):
    return render(request, 'pages/about_app.html')

def app_contact(request):
    return render(request, 'pages/contact_app.html')

def lession_details(request, lession_id):
    lession1 = get_object_or_404(lessions, id=lession_id)
    return render(request, 'pages/lession_detailes.html', {'lession1': lession1})
