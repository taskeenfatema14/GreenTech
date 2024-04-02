from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView
from portals.constants import *

class ImageApi(APIView):
    # serializer_class = LandingImageSerializer
    # model = LandingImage
    # related_models = {}
    # allowed_methods = [GET, GETALL, POST, PUT, DELETE]

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

    
# class GetOneImageApi(APIView):
#     def get(self, request):
#         # Retrieve only the first image
#         image = LandingImage.objects.first()    
#         # If an image is found
#         if image:
#             # Construct the response in the expected format
#             response_data = [{"url": image.image.url}]
#             return Response(response_data, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "No image found"}, status=status.HTTP_404_NOT_FOUND)



class CategoryApi(APIView):
    # serializer_class = CategorySerializer
    # model = Category
    # related_models = {}
    # allowed_methods = [GET, GETALL, POST, PUT, DELETE]

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

from django.http import Http404

class CategoryDetailApi(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryPutApi(APIView):
    def put(self, request,id):
        try:
            instance = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response({"error" : "Cateogory not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            instance = Category.objects.get(pk=id)
            instance.delete()
            return Response({"message" : "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPIViewPagination(APIView):
    def get(self, request):
        params = request.GET
        page_number = int(params.get("pg", 1))
        page_size = int(params.get("limit", 2 ))
        offset = (page_number - 1) * page_size
        limit = page_size

        cat = Category.objects.all()
        paginated_category = cat[offset:offset + limit]
        all_category_data = []
        for c1 in paginated_category:            
            # campaign_image_url = c1.image.url if c1.image else None
            api_data = {
                'category image': c1.image.url,
                'title':c1.title,
            }
            all_category_data.append(api_data)
        return Response(all_category_data, status=status.HTTP_200_OK)
    

