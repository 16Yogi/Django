from django.http import HttpResponse
from django.shortcuts import render
from . import views
from .models import lession6
from django.shortcuts import get_object_or_404

def all_lession(request):
    lession = lession6.objects.all()
    return render(request,'app_index.html',{'lession':lession})
    # return render(request,'app_index.html')
    # return HttpResponse("This is all Lession")

def app_about(request):
    return render(request,'pages/app_about.html')
    # return HttpResponse("This is app about secation")

def app_contact(request):
    return render(request,'pages/app_contact.html')
    # return HttpResponse("This is app contact secation")

def lession_details(request,lession_id):
    lession1 = get_object_or_404(lession6,id=lession_id)
    return render(request,'pages/lession_details.html',{'lession1':lession1})
