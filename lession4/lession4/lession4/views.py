from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("This is home secation")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is about secation")
    return render(request,'pages/about.html')

def contact(request):
    # return HttpResponse("This is contact secation")
    return render(request,'pages/contact.html')

