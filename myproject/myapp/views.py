from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import RazorpayOrder
import razorpay
from .utils import send_sms_message
from random import randint

from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Extracting username and phone number from the form
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            # Sending SMS notification
            sms_phone_number = "+91" + phone_number  # Adding +91 for sending SMS
            message = f"Your account was successfully created in KGH-Bites.\nUsername: {username}\nPhone number: {phone_number}"
            # Sending SMS message using your preferred SMS gateway or service
            send_sms_message(sms_phone_number, message)
            # Displaying success message
            messages.success(request, f'Account was created for {username}')
            return redirect('login')  # Use the URL pattern name here
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

from .utils import send_payment_failed_sms

def main_checkout(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    order = RazorpayOrder()

    data = {
        "amount": randint(100, 500),
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture": "1",
    }
    payment = client.order.create(data=data)
    order.rp_order_id = payment['id']
    
    # Render the main checkout page
    context = {"payment": payment}
    return render(request, 'maincheckout.html', context)

def capture_payment(request):
    if request.method == 'POST':
        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
            payment_id = request.POST.get('payment_id')
            amount = request.POST.get('amount')
            
            # Attempt to capture the payment
            capture = client.payment.capture(payment_id, amount)
            if capture['status'] == 'captured':
                # Payment successful
                return redirect('payment_success')  # Redirect to a success page if needed
            else:
                # Payment failed
                phone_number = request.POST.get('phone_number')  # Get the entered phone number from the form
                send_payment_failed_sms(phone_number)  # Send payment failure SMS
                return redirect('payment_failed')  # Redirect to the payment failure page
        except Exception as e:
            print(f"Exception occurred during payment capture: {str(e)}")
            return redirect('payment_failed')  # Redirect to the payment failure page
    else:
        # Handle GET request for capture_payment view
        return redirect('main_checkout')  # Redirect to the main checkout page if accessed via GET

    
def send_payment_failed_sms(phone_number):
    try:
        # Send SMS notification for payment failure to the entered phone number
        send_sms_message(phone_number, "Payment failed for order. Please check.")
    except Exception as e:
        print(f"Failed to send SMS notification for payment failure. Error: {str(e)}")    


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




def misc_checkout(request):
    
    order = RazorpayOrder()
    
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

    DATA = {
        "amount": randint(100,500),
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture":"1",
    }
    payment = client.order.create(data=DATA)
    order.rp_order_id = payment['id']
    print(payment)
    context = {"payment":payment}
    return render(request, 'misccheckout.html', context)

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

def payment_failed(request):
    return render(request,'payment_failed.html')