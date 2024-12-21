from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Home secation")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("About secation")
    return render(request,'pages/about.html')

def contact(request):
    # return HttpResponse("Contact secation")
    return render(request,'pages/contact.html')

