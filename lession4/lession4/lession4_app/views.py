from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def lession4_all(request):
    # return HttpResponse("Hello This is all lession")  
    return render(request,'app_index.html')  

def lession4_about(request):
    return render(request,'pages/app_about.html')

def lession4_contact(request):
    return render(request,'pages/app_contact.html')


