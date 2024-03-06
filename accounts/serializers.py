from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *

class UserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'