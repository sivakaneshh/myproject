from twilio.rest import Client
from django.conf import settings

def send_sms_message(to_number, message):
    # Your Twilio credentials
    #account_sid = settings.TWILIO_ACCOUNTSID
    #auth_token = settings.TWILIO_AUTHTOKEN
    #twilio_phone_number = settings.TWILIO_PHONENUMBER

    # Initialize Twilio client
    #client = Client(account_sid, auth_token)

    #try:
        # Send SMS message using Twilio
       # client.messages.create(
        #    to=to_number,
        #    from_=twilio_phone_number,
        #    body=message
       # )
    #except Exception as e:
        # Handle any errors that occur during message sending
     #   print(f"Error sending SMS: {str(e)}")