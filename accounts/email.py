from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
from datetime import datetime, timedelta

def send_otp_via_email(email):
    subject = 'Your Account Verification'
    otp=random.randint(1000, 9999)
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email], fail_silently=False)
    # Save the OTP to the database
    user_obj, created = User.objects.get_or_create(email=email)
    user_obj.otp = otp
    user_obj.save()