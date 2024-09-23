from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
    
        user = authenticate(request,username = uname, password = pswd)
        if user is not None:
            user = login(request,user)
            return redirect('Index')
        else:
            messages.error(request,"username or password in correct")
            return redirect("SignIn")
        
    else:
        return render(request,"login.html")
    
def SignOut(request):
    logout(request)
    return redirect("Index")

def Index(request):
    video = VideoSlide.objects.all().last()
    context = {
       "video":video 
    }
    return render(request,"index.html",context)

def AboutUs(request):
    return render(request,'aboutus.html')

def Service_Architecture(request):
    return render(request,"archituture_service.html")

def Service_InteriorDesign(request):
    return render(request,"interior_design_service.html") 

def Service_Civil_Construction(request):
    return render(request,"civil_contstruction_service.html") 

def Service_Renovation(request):
    return render(request,"renovation_service.html") 

def Blog(request):
    return render(request,"blog.html") 

def Contact(request):
    return render(request,"contact.html")

def Gallery(request):
    return render(request,"gallery.html")

def Projects(request):
    return render(request,"projects.html")
