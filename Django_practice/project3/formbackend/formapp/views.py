from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import user
# Create your views here.
@csrf_exempt
def savedata(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            print("not run")

        username = data.get("username")
        useremail = data.get("email")
        userpassword = data.get("password")
        savedata = user(
            Name = username,
            Email = useremail, 
            password = userpassword
        )
        savedata.save()
    # else:
        
    # re
            

        