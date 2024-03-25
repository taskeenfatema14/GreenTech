from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers 
from .models import * 

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'title']

class ProductSerializer1(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','image', 'title']

        
class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'description', 'image', 'title']

class ProductSerializer(serializers.ModelSerializer):
    prodectitems = ProductItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'prodectitems']

class ProductListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title']

        
class BrochureSerializer(ModelSerializer):
    class Meta:
            model  = Brochure
            fields = ['productitem', 'detail', 'image']