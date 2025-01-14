from django.shortcuts import render
from .models import Project5
from .forms import Project5Form
from django.shortcuts import get_object_or_404,redirect


# Create your views here.
def home(request):
    return render(request,'index.html')

def project5_list(request):
    tweets = Project5.objects.all().order_by('-created_at') #this help to access
    return render(request,'tweet_list.html',{'tweets':tweets})

def project5_create(request):
    if request.method=="POST":
        form = Project5Form(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user 
            tweet.save()
            return redirect('project5_list')
    else:
        form = Project5Form()
    return render(request,'tweet_list.html',{'form':form})

def project5_edit(request,tweet_id):
    tweet = get_object_or_404(Project5,pk=tweet_id,user=request.user) 
    if request.method == 'POST':
        form = Project5Form(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user 
            tweet.save()
            return redirect('project5_list')
    else:
        form = Project5Form(instance=tweet)
    return render(request,'tweet_list.html',{'form':form})

def project5_delete(request,tweet_id):
    tweet = get_object_or_404(Project5,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('project5_list')
    # else:
        # form = Project5Form(instance=tweet)
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def registation(request):
    return render(request,'registration/register.html')

def login(request):
    return render(request,'registration/login.html')

def logout(request):
    return render(request,'registration/logout.html')

def tweet_list(request):
    return render(request,'tweet_list.html')