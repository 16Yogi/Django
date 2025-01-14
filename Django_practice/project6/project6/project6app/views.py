from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def movie_create(request):
    if request.method=="POST":
        form = MovieUpload(request.POST,request.FILES) 
        if form.is_valid():
            # movie = form.save(commit=False) 
            # movie.user = request.user 
            # movie.save()
            return redirect('index')
    else:
        form = MovieUpload() 
    return render(request,'movie_from.html',{'form':form})


def movie_list(request):
    movie_lists = MovieListForm.objects.all().order_by('-create_at')
    return render(request,'index.html',{'movie_lists':movie_lists})
    

def registration(request):
    if request.method=="Post":
        if form.is_valid():

            return('index')
    else:
        form = UserRegistration()
    return render(request,'registration/register.html',{'form':form})

def allUser(request):
    allUser = RegistrationForm.objects.all()
    return render(request,'allUser.html',{'allUser':allUser})

def login(request):
    return render(request,'registration/login.html')

def logout(request):
    return render(request,'registration/logout.html')

def testfrom(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return render(request, 'test_form.html', {'form': form, 'success': True})
    else:
        form = TestForm() 
    return render(request, 'test_form.html', {'form': form})
