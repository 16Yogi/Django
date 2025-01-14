from django.shortcuts import render
# 
from .models import Project 
from .forms import ProjectForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
# 
from django.contrib.auth.decorators import login_required
# login
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(request,'index.html')

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request,'project_list.html',{'projects':projects})

@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request,'project_form.html',{'form':form})

# def prject_edit(request,project_id):
#     project = get_object_or_404(Project,pk=project_id,user = request.user) 
#     if request.method == 'POST':
#         form = ProjectForm(request.POST,request.FILES,instance=project),
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = request.user 
#             project.save()
#             return redirect('project_list')
#     else:
#         form = ProjectForm(instance=project)
#     return render(request,'project_form.html',{'form':form}) 

@login_required
def project_edit(request, project_id):  
    project = get_object_or_404(Project, pk=project_id, user=request.user) 
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project) 
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user 
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})

# @login_required
# def project_delete(request,project_id):
#     get_object_or_404(Project,pk=project_id,user=request.user)
#     if request.method == 'POST':
#         project.delete()
#         return redirect('project_list')
#     return render(request,'project_confirm_delete.html',{'project':project}) 

# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Project
@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id,user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  
    return render(request, 'project_confirm_delete.html', {'project': project})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('project_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

    
