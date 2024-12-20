from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello This is home")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("Hello this is about")
    return render(request,'pages/about.html')

def contact(request):
    # return HttpResponse("This is contact secation")
    return render(request,'pages/contact.html')

def layout(request):
    # return render(request,'layout.html')
    return render(request,'layout.html')