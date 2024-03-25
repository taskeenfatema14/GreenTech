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

class CategorySerializer1(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']



# from rest_framework.fields import UUIDField

# class BrochureSerializer(ModelSerializer):
#     product_id = UUIDField(write_only=True)  # Using UUIDField for product_id
#     class Meta:
#         model  = Brochure
#         fields = ['product_id', 'detail', 'image']

#     def create(self, validated_data):
#         product_id = validated_data.pop('product_id', None)
#         if product_id is not None:
#             validated_data['product'] = Product.objects.get(pk=product_id)
#         return super().create(validated_data)
    


    
