from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User , auth
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

def home(request):
    return render(request,'lali.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method =='POST':
        user_name = request.POST["user_name"]
        pwd = request.POST["pwd"]
        role=request.POST["role"]
        user = auth.authenticate(user_name=user_name,pwd=pwd)
        if user is not None:
            auth.login(request,user)
        if role=="mentee":
            return redirect('register')
        if role=="mentor":
            return redirect('register')
        if role=="intern":
            return redirect('register')
    
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def dboard(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>Hi</h1>")
    else:
        return HttpResponse("<h1>Nope</h1>")


