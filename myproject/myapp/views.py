from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

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

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Username or password is incorrect")
            
    context = {}
    return render(request, 'login.html', context)

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
    import razorpay
    client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

    DATA = {
        "amount": 100,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
    }
    client.order.create(data=DATA)
    
    return render(request, 'checkout.html')

def conformation(request):
    return render(request,'conformation.html')