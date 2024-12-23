from django.shortcuts import render
from django.http import HttpResponse
from .models import lessions
from django.shortcuts import get_object_or_404
# Create your views here.

def all_app(request):
    # return HttpResponse("All Appp")
    lession = lessions.objects.all()
    return render(request,'all_app.html',{'lession':lession})

def lession_details(request, lession_id):
    # Corrected: Use 'id' instead of 'lessa'
    lession1 = get_object_or_404(lessions, id=lession_id)
    return render(request, 'pages/lession_detailes.html', {'lession1': lession1})


def app_about(request):
    # return HttpResponse("ABout")
    return render(request,'pages/app_about.html')