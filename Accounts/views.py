from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import login,authenticate,logout
from .models import *



# Create your views here.

def HomeView(request):
    #return HttpResponse("Accounts App")
    return render(request,'index.html')

def signup(request):
     if request.method == 'POST':
   
       fullname=request.POST['fullname']
       email=request.POST['email']
       password=request.POST['password']
       confirm_password=request.POST['confirm_password']

       if password != confirm_password:
           messages.error(request,"password do not match")
           return redirect('/user/signup/')
       
       if User.objects.filter(email=email).exists():
           messages.error(request," Email already Registerd")
           return redirect('/user/signup/')
       
       email_username=email.split('@')[0]
       
       myuser=User.objects.create_user(email_username, email, password)
       myuser.first_name=fullname
       myuser.save()
       Profile.objects.create(user=myuser)
       messages.success(request,"Account created successfully")
       return redirect('/user/signup/')
     else:
         return render(request,'auth/signup.html')
     
def loginViews(request):
    if request.method == 'POST':
        email1=request.POST.get('email1')
        password=request.POST.get('password')
        
        user_obj = User.objects.get(email=email1)
        username = user_obj.username
    
        user=authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in!')
            return redirect('/')
        else: 
            messages.error(request, 'Invalid email or password')
    return render(request, 'auth/login.html')

def logoutViews(request):
    logout(request)
    messages.error(request, "Successfully logged out")
    return redirect('/')

           

       



