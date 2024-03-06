from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ImageApi(APIView):
    def post(self, request):
        serializer = LandingImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        camp = LandingImage.objects.all()
        serializer = LandingImageSerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetOneImageApi(APIView):
    def get(self, request):
        # Retrieve only the first image
        image = LandingImage.objects.first()    
        # If an image is found
        if image:
            # Construct the response in the expected format
            response_data = [{"url": image.image.url}]
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No image found"}, status=status.HTTP_404_NOT_FOUND)

class CategoryApi(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        camp = Category.objects.all()
        serializer = CategorySerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    