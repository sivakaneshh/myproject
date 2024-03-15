from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from twilio.rest import Client
from django.shortcuts import render
#from .utils import send_sms_message

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Extracting username and phone number from the form
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            # Sending SMS notification
            message = f"Your account was successfully created in KGH-Bites.\nUsername: {username}\nPhone number: {phone_number}"
            send_sms_message(phone_number, message)
            # Displaying success message
            messages.success(request, f'Account was created for {username}')
            return redirect('login')  # Use the URL pattern name here
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


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

def conformation(request):
    return render(request,'conformation.html')

def addmin(request):
    return render(request, 'addmin.html')

def inventory(request):
    return render(request,'inventory.html')

def additems(request):
    return render(request,'additems.html')

def maincheckout(request):
    return render(request,'maincheckout.html')

def misccheckout(request):
    return render(request, 'misccheckout.html')

