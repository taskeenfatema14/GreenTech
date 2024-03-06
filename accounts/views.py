from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import *

from portals.services import generate_token
from django.contrib.auth.hashers import check_password



class RegisterApi(APIView):
     def post(self,request,*args, **kwargs):
        try : 
            serializer = UserSerializer(data=request.data)
            if  serializer.is_valid():
                serializer.save()
                return Response({"message" : "User Created Succefully" , "data" : serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            raise ValidationError({
                "status_code" : status.HTTP_400_BAD_REQUEST,
                "message" :  e
            })

     def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# class LoginAPi(APIView):
#     def post(self,request,*args, **kwargs):
#             email       = request.data.get('email')
#             password    = request.data.get('password')
#             # Generate Token
#             user = User.objects.filter(email=email).first()
#             print
#             if user is None : 
#                 return Response({"error" : False,"data" : "User Not Exists"},status=status.HTTP_404_NOT_FOUND)
#             token = generate_token(user.email)
#             # password_match = check_password(password,user.password)
#             password_match = check_password(password,user.password)
#             print("password match",password_match)
#             serializer = UserSerializer(user)
#             data = {"error" : False, "message": "User logged in successfully","user_info": serializer.data,"token" : token}
#             if password == user.password  or password_match:
#                 return Response(data,status=status.HTTP_200_OK)
#             else :
#                 return Response({"error" : True, "message" : "Something Went Wrong"},status=status.HTTP_400_BAD_REQUEST)
            

class LoginAPi(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": True, "message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if password != user.password:
            return Response({"error": True, "message": "Incorrect password."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(user)
        return Response({"error": False, "message": "User logged in successfully", "user_info": serializer.data}, status=status.HTTP_200_OK)