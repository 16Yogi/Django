from django.shortcuts import render
from .models import Project2
from .forms import UserRegistrationForm,ProjectForm 
from django.shortcuts import get_object_or_404,redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
# def showUser(request):
    # return render(request,'alluser.html')

# this is for home page
def allUser_view(request):
    allusers = Project2.objects.all().order_by('-create_at')
    return render(request,'alluser.html',{'allusers':allusers})

# this is for all user
def regUsers(request):
    all_users = User.objects.all()
    return render(request, 'printRegis.html', {'all_users': all_users})

# this is registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('alluser')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

# this is for update
@login_required
def user_edit(request,project_id):
    project = get_object_or_404(Project2,pk=project_id,user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project) 
        if form.is_valid():
            project = form.save(commit=False) 
            project.user = request.user
            project.save()
            return redirect('alluser')
    else:
        form = ProjectForm(instance=project)
    return render(request,'user_edit.html',{'form':form})

# create update 
def create_update(request,project_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        project = form.save(commit=False)
        project.user = request.user 
        project.save()
        return redirect('alluser')        
    else:
        form = ProjectForm()
    return render(request,'user_edit.html',{'form':form})

