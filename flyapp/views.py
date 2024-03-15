from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'flyapp/home.html')

def profile(request):
    if User.is_authenticated:
        return render(request, 'flyapp/profile.html')
    else:
        return redirect('flyapp:login_customer')

def meetTheTeam(request):
    return render(request, 'flyapp/meetTheTeam.html')

def register_customer(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration complete"))
            return redirect('flyapp:home')
    else:
        form = RegisterUserForm()
    
    return render(request, 'flyapp/register_customer.html', {'form':form})

def login_customer(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in ... quack! quack!")
            return redirect('flyapp:home')
        else:
            messages.success(request,("There was an error logging in, Try Again..."))
            return redirect('flyapp:login_customer')
    else:
        return render(request, 'flyapp/login.html', {})

def logout_customer(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('flyapp:home') 


