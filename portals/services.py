
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