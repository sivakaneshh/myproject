# utils.py

from twilio.rest import Client
from django.conf import settings

def send_sms_message(to_number, message):
    # Your Twilio credentials
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Send SMS message using Twilio
        client.messages.create(
            to=to_number,
            from_=twilio_phone_number,
            body=message
        )
    except Exception as e:
        # Handle any errors that occur during message sending
        print(f"Error sending SMS: {str(e)}")
        
def send_payment_failed_sms(to_number, message):
        # Your Twilio credentials
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Send SMS message using Twilio
        client.messages.create(
            to=to_number,
            from_=twilio_phone_number,
            body=message
        )
    except Exception as e:
        # Handle any errors that occur during message sending
        print(f"Error sending SMS: {str(e)}")