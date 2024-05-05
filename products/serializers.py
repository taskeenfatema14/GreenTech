from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers 
from .models import * 

class ProductSerializer1(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','image', 'title']
        
class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['id','product', 'description', 'image', 'title']

class ProductBrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = ['id','brochure']

class ProductItemBrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Brochure
        fields = ['id']
class ProductItemSerializer1(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    prodectitems = ProductItemSerializer(many=True, read_only=True)
    brochure = ProductItemBrochureSerializer(many=True,read_only=True)

    # brochure_id = serializers.PrimaryKeyRelatedField(source='brochure', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'prodectitems', 'brochure']

class ProductListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'id']

        