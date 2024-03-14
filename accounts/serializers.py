from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password



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


from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User


# User = get_user_model()

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


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

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
