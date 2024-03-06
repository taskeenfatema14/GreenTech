from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers 
from .models import * 

class LandingImageSerializer(ModelSerializer):
    class Meta:
        model = LandingImage
        fields = ['image', 'video']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['image', 'title','link']