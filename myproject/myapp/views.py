# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def maincanteen(request):
    return render(request,'maincanteen.html')

def misccanteen(request):
    return render(request,'misccanteen.html')

