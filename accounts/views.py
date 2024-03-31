from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import *

from portals.services import generate_token
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password



# class RegisterApi(APIView):
#      def post(self,request,*args, **kwargs):
#         try : 
#             serializer = UserSerializer(data=request.data)
#             if  serializer.is_valid():
#                 serializer.save()
#                 return Response({"message" : "User Created Succefully" , "data" : serializer.data},status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e :
#             raise ValidationError({
#                 "status_code" : status.HTTP_400_BAD_REQUEST,
#                 "message" :  e
#             })
        
# Create your views here.

class RegisterApi(APIView):
    def post(self, request):
        try:
            data = request.data.copy()
            if 'password' in data and 'confirm_password' in data:
                if data['password'] != data['confirm_password']:
                    print("password check")
                    return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
                data.pop('confirm_password')
            print("here it is")
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                print("serializer check")
                serializer.save()
                print("serializer check")
                return Response({"message": "User Created Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

##################  working for user...
    
# class LoginAPI(APIView):
#     def post(self,request,*args, **kwargs):
#             email       = request.data.get('email')
#             password    = request.data.get('password')
#             user = User.objects.filter(email=email).first()
#             print(user)
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
            

class LoginAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({"error": False, "data": "User Not Exists"}, status=status.HTTP_404_NOT_FOUND)

        if user.is_admin:
            # If user is an admin, proceed with admin authentication
            password_match = check_password(password, user.password)
            if password_match:
                token = generate_token(user.email)
                serializer = UserSerializer(user)
                data = {
                    "error": False,
                    "message": "Admin logged in successfully",
                    "admin_info": serializer.data,
                    "token": token
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": True, "message": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If user is not an admin, proceed with regular user authentication
            if user.check_password(password):
                token = generate_token(user.email)
                serializer = UserSerializer(user)
                data = {
                    "error": False,
                    "message": "User logged in successfully",
                    "user_info": serializer.data,
                    "token": token
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": True, "message": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)


#############################  CHANGE PASSWORD   ####################################################

class ChangePasswordApi(APIView):
    def post(self,request,*args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={'request': self.request})
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Password updated successfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#############################  FORGET PASSWORD   ####################################################
from .email import *

# class ForgotPasswordApi(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = ForgotPasswordSerializer(data=data)
#             print(serializer)

#             if serializer.is_valid():
#                 send_otp_via_email(serializer.validated_data['email'])
#                 print("valid")

#                 return Response({
#                     'status': 200,
#                     'message': 'OTP sent successfully.',
#                     'data': serializer.validated_data,
#                 })

#             return Response({
#                 'status': 400,
#                 'message': 'Something went wrong',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
#             return Response({
#                 'status': 500,
#                 'message': 'Internal Server Error',
#                 'data': str(e),
#             })


# from random import randint
# from django.core.mail import send_mail
# from portals.services import generate_token,my_mail

# class ForgotPasswordApi1(APIView):
#     def post(self,request,*args, **kwargs):
#         try :
#             mail = request.data.get('email')
#             print("in user",mail)
#             user = User.objects.get(email=mail)
#             print(user)
#             otp = randint(1000,9999)
#             res = my_mail(mail,otp)
#             if (res ==1):
#                 return Response(data={'Success':'Otp Mail sent succesfully to '+ mail,'OTP':str(otp)},status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": True,"message" : "Error sending Mail"},status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({"error": True,"message" : "User Email Does not exists"},status=status.HTTP_400_BAD_REQUEST )

# class ResetPasswordAPI(APIView):
#     def post(self,request,*args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         if User.objects.filter(email=email):
#             user = User.objects.get(email=email)
#             user.set_password(password)
#             user.save()
#             return Response(data={'Success':'Password for Email ' +str(user) +' reset succesfull'},status=status.HTTP_200_OK)
#         return Response(data = {'Error':'Email does not exists'})



#******************************************************************************#
# class VerificationOtpApi(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyForgotOTPSerializer(data=data)
#             print(serializer)

#             if serializer.is_valid():
#                 return Response({
#                     'status': 200,
#                     'message': 'OTP verification successful.',
#                     'data': serializer.validated_data,
#                 })

#             return Response({
#                 'status': 400,
#                 'message': 'OTP verification failed',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
#             return Response({
#                 'status': 500,
#                 'message': 'Internal Server Error',
#                 'data': str(e),
#             })
        

# class VerificationOtpApi(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyOTPSerializer(data= data)

#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 otp = serializer.data['otp']
#                 print(otp)

#                 user = User.objects.filter(email=email).first()

#                 if not user:
#                     return Response({
#                         'status': 400,
#                         'message': 'User not found',
#                         'data': 'Invalid email',
#                     })

#                 if otp != otp:
#                     print("wrong otp")
#                     return Response({
#                     'status': 400,
#                     'message': 'something went wrong',
#                     'data': 'wrong otp'
#                 })

#                 user.is_verified = True
#                 user.save()

#                 return Response({
#                     'status': 200,
#                     'message': 'Email Verification is done successfully...',
#                     'data': serializer.data,
#                 })
            
#             return Response({
#                 'status': 400,
#                 'message': 'something went wrong',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
#             return Response({
#                 'status': 500,
#                 'message': 'Internal Server Error',
#                 'data': str(e),
#             })

        
# #******************************************************************************#
# class SetNewPasswordApi(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = SetNewPasswordSerializer(data=data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({
#                     'status': 200,
#                     'message': 'Password reset successful.',
#                     'data': serializer.validated_data,
#                 })

#             return Response({
#                 'status': 400,
#                 'message': 'Password reset failed.',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
#             return Response({
#                 'status': 500,
#                 'message': 'Internal Server Error',
#                 'data': str(e),
#             })



#######################  Admin Registration  ####################

class AdminLoginView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#######################  Enquiry  ####################

# Working api w/o login checkup 
# class EnquiryApi(APIView):
#     def post(self, request):
#         serializer = EnquirySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Enquiry is send", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.permissions import IsAuthenticated

class EnquiryApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            # Automatically set the user based on the authenticated user
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response("Enquiry is sent", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # working with is_admin = trure

# class LoginAPI(APIView):
#     def post(self, request):
#         # Check if the request is for admin login
#         if 'is_admin' in request.data and request.data['is_admin']:
#             serializer = AdminLoginSerializer(data=request.data)
#             if serializer.is_valid():
#                 return Response({'message': 'Admin login successful'}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:  # Assuming non-admin login
#             email = request.data.get('email')
#             password = request.data.get('password')
#             print(email)
#             print(password)
#             user = User.objects.filter(email=email).first()
#             print(user)
#             if user is None:
#                 return Response({"error": True, "message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
#             if check_password(password, user.password):
#                 serializer = UserSerializer(user)
#                 token = generate_token(user.email)  # Implement your token generation logic
#                 data = {"error": False, "message": "User logged in successfully", "user_info": serializer.data, "token": token}
#                 return Response(data, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": True, "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



#working for admin as user.... 

# class LoginAPI(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         print(email)
#         print(password)

#         if self.is_admin_credentials(email, password):
#             serializer = AdminLoginSerializer(data=request.data)
#             if serializer.is_valid():
#                 return Response({'message': 'Admin login successful'}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:  
#             user = User.objects.filter(email=email).first()
#             print(user)
#             print("user")
#             if user is None:
#                 return Response({"error": True, "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#             if not check_password(password, user.password):
#                 return Response({"error": True, "message": "Incorrect password."}, status=status.HTTP_401_UNAUTHORIZED)
#             print("In side passwrod match")
#             serializer = UserSerializer(user)
#             # token = generate_token(user.email) 
#             data = {"error": False, "message": "User logged in successfully", "user_info": serializer.data, }
#             return Response(data, status=status.HTTP_200_OK)
#             # else:
#             #     print(f"Invalid password for user with username {username}.")
#             #     return Response({"error": True, "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#     def is_admin_credentials(self, email, password):
        
#         admin_email = "admin123@gmail.com"
#         admin_password = "admin12345"
#         return email == admin_email and check_password(password, admin_password)
        


###########      komal's login code

# class LoginAPI(APIView):
#     def post(self, request):
#         email = request.data.get('email')  # Use 'email' as the key
#         password = request.data.get('password')
#         print(email)
#         print(password)
#         # Authenticate the user
#         user = authenticate(request, email=email, password=password)
#         print(user)

#         if user:
#             return Response({
#                 'user_id': user.pk,
#                 'email': user.email,
#                 'name': user.name,  # Include any other fields you want to return
#                 'message': 'Successfully logged in'
#             })
#         else:
#             # If authentication failed, return error message
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
################## Working Code  #################### 

class ForgotPasswordApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ForgotPasswordSerializer(data=data)

            if serializer.is_valid():
                send_otp_via_email(serializer.validated_data['email'])

                return Response({
                    'status': 200,
                    'message': 'OTP sent successfully.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })
        
    def get(self, request):
        serializer = ForgotPasswordSerializer(data=request.query_params)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            # Process the email (e.g., send reset password email)
            return Response({"message": "Password reset email sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#**************************#
class VerificationOtpApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyForgotOTPSerializer(data=data)

            if serializer.is_valid():
                return Response({
                    'status': 200,
                    'message': 'OTP verification successful.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'OTP verification failed',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })
        
#**************************#
class SetNewPasswordApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = SetNewPasswordSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Password reset successful.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'Password reset failed.',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })