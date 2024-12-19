from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django. You are at Yogi's home PC")
    return render(request,'index.html')


def about(request):
    # return HttpResponse("Hello, Django. You are at Yogi's about PC")
    return render(request,'pages/about.html')

def contact(request):
    return HttpResponse("Hello, Django. You are at Yogi's contact PC")


