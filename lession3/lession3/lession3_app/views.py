from django.shortcuts import render

# Create your views here.
def all_lession(request):
    return render(request,'lession3_app/all_lession.html')