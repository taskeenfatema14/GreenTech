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
        fields = ['product', 'description', 'image', 'title']

class ProductItemSerializer1(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    prodectitems = ProductItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'prodectitems']

class ProductListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'id']

        
class BrochureSerializer(ModelSerializer):
    class Meta:
            model  = Brochure
            fields = ['productitem', 'detail', 'image']