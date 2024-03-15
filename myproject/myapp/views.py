from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')  # Use the URL pattern name here
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        
        
        # Authenticate using phone number instead of username
        user = authenticate(request, phone_number=phone_number, password=password)
        user = User.objects.filter(email=phone_number).first()
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Phone number or password is incorrect")
            
    return render(request, 'login.html')

def addmin_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        
        
        # Authenticate using phone number instead of username
        user = authenticate(request, phone_number=phone_number, password=password)
        user = User.objects.filter(email=phone_number).first()
        
        if user is not None:
            auth_login(request, user)
            return redirect('addmin')
        else:
            messages.info(request, "Phone number or password is incorrect")
            
    return render(request, 'addmin_login.html')
        
        





def user_logout(request):
    logout(request)
    return redirect('login')
    
def home(request):
    return render(request, 'home.html')

def maincanteen(request):
    return render(request, 'maincanteen.html')

def misccanteen(request):
    return render(request, 'misccanteen.html')

def checkout(request):
    return render(request, 'checkout.html')

def conformation(request):
    return render(request,'conformation.html')

def addmin(request):
    return render(request, 'addmin.html')

def inventory(request):
    return render(request,'inventory.html')

def additems(request):
    return render(request,'additems.html')