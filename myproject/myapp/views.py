from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import get_user_model

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

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        # Query the user by matching the phone number with the email field
        user = User.objects.filter(email=phone_number).first()
        
        # Authenticate the user with the provided password
        if user is not None and user.check_password(password):
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Phone number or password is incorrect")  # Update error message
            
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
    
def index(request):
    return render(request, 'index.html')

def maincanteen(request):
    return render(request, 'maincanteen.html')

def misccanteen(request):
    return render(request, 'misccanteen.html')
def checkout(request):
    return render(request, 'checkout.html')
def conformation(request):
    return render(request,'conformation.html')