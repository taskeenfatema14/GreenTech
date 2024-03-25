from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_admin','created_on','updated_on']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract the password from validated_data
        password = validated_data.pop('password')
        
        # Create a new user instance with the remaining data
        user = User.objects.create_user(**validated_data)
        
        # Hash the password and set it for the user
        user.set_password(password)
        
        # Save the user object
        user.save()
        
        return user  


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(username=email).first()
        if user and user.check_password(password):
            return attrs
        else:
            raise serializers.ValidationError('Invalid email or password.')



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')

        if not email:
            raise ValidationError({'message': 'Email is required.'})

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError({'message': 'Email not found in the database.'})

        return data
    
class VerifyForgotOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp').strip()
        print(otp)

        if not (email and otp):
            raise ValidationError({'message': 'Email and OTP are required.'})

        user = User.objects.filter(email=email).first()
        print(user)

        if not user or user.otp != otp:
            print("in this not equal block")
            raise ValidationError({'message': 'Invalid email or OTP.'})

        return data
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')

        if not email:
            raise ValidationError({'message': 'Email is required.'})

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError({'message': 'Email not found in the database.'})

        return data
    
class VerifyForgotOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')

        if not (email and otp):
            raise ValidationError({'message': 'Email and OTP are required.'})

        user = User.objects.filter(email=email).first()

        if not user or otp != otp:
            raise ValidationError({'message': 'Invalid email or OTP.'})

        return data
    
class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not (new_password and confirm_password):
            raise ValidationError({'message': 'New password and confirm password are required.'})

        if new_password != confirm_password:
            raise ValidationError({'message': 'New password and confirm password do not match.'})

        return data
    
    def save(self):
        print("Save")
        email = self.context.get('email')  # Retrieve email from context
        user = User.objects.get(email=email)
        user.set_password(self.validated_data['new_password'])
        user.save()
        print("Save1")


User = get_user_model()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_old_password(self, old_password):
        user = self.context['request'].user
        if not user.is_authenticated:
            raise serializers.ValidationError("User is not authenticated.")
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")
        return old_password

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Incorrect username or password')

        return attrs
    
    def create(self, validated_data):
        # Extract the password from validated_data
        password = validated_data.pop('password')
        
        # Create a new user instance with the remaining data
        user = User.objects.create_user(**validated_data)
        
        # Hash the password and set it for the user
        user.set_password(password)
        
        # Save the user object
        user.save()


class EnquirySerializer(ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'





