from django.shortcuts import render
from django.db import models
from .models import Form 
from .forms import DashboardForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect 
from django.contrib.auth import login
from django.contrib.auth.models import User
# from django.contrib.auth import login_required  

# Create your views here.
def dashboard_view(request):
    return render(request,'dashboard.html')

def user_list(request):
    users = Form.objects.all().order_by('-create_at')
    return render(request,'user_list.html',{'users':users})

def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('user_list')
    else:
        form = UserRegistrationForm()
    return render(request,'pages/register.html',{'form':form})

def login_view(request):
    return render(request, 'pages/login.html')

def logout_view(request):
    return render(request, 'pages/logged_out.html')