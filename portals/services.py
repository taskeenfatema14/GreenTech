
import jwt
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives

def generate_token(email):
    payload = {
        "email" :email
    }
    token = jwt.encode(payload, "asdfghjkhgfdsasdrtyu765rewsazxcvbnjkio908765432wsxcdfrt", algorithm="HS256")
    return token


def my_mail(mail, otp):
    subject = "Fairseed Password Reset OTP"
    msg = "Your one-time password for resetting the password at <strong>Fairseed</strong> is as follows: <strong>{}</strong> <br>\nPlease do not share this with anyone.".format(otp)
    
    # Create an EmailMultiAlternatives object to support HTML content
    email = EmailMultiAlternatives(subject, msg, '33azharoddin@gmail.com', [mail])
    email.attach_alternative(msg, "text/html")  # Specify HTML content type
    
    try:
        res = email.send()
        print("Email sent successfully:", res)
        if res == 1:
            msg = 1
        else:
            print("Email not sent")
            msg = 0
    except Exception as e:
        print("Error sending email:", e)
        msg = 0
        
    return msg