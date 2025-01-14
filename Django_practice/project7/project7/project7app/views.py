from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def registration1(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_registration1(request,user_id):
    form = get_object_or_404(Registration,pk=user_id,user=request.user)
    if request.method=='POST':
        form = RegistrationForm(request.POST,request.FILES,instance=form)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.user = request.user 
            user_data.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    
@login_required
def delete_registration1(request,user_id):
    form = get_object_or_404(Registration,pk=user_id,user=request.user)
    if request.method == 'POST':
        user_data.delete()
        return redirect('index')
    return render(request,'delete_confirm.html',{'form':form})

@login_required
def reg1_user_list(request):
    form_data = Registration.objects.all()
    return render(request,'reg_user.html',{'form_data':form_data})

@login_required
def registertion2(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Registration2.objects.create(
            fname = fname,
            email = email,
            password = password
        )
        return render(request,'index.html',{'message': 'Registration successful!'})
    return render(request,'registration/register2.html')

def reg2_user_list(request):
    form_data = Registration2.objects.all()
    return render(request,'reg2_user.html',{'form_data':form_data})


def adminReg(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login(request,user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/admin_reg.html',{'form':form})
