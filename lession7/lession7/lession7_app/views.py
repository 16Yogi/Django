from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import lessions,Store
from .forms import lessionVerityForm
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


# def lession_store_view(request):
    # return HttpResponse("Hello")
    # return render(request, 'pages/lession_store.html')


def lession_store_view(request):
    stores = None
    if request.method == 'POST':
        form = lessionVerityForm(request.POST)
        if form.is_valid():
            lession_verity = form.cleaned_data['lession_verity']
            stores = Store.objects.filter(lession_list=lession_verity)
    else:
        form = lessionVerityForm()
    return render(request, 'pages/lession_store.html',{'stores':stores,'form':form})