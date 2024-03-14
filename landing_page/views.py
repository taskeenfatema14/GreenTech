from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
import math
from rest_framework.pagination import PageNumberPagination


# Create your views here.
################  Image  ########################

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


################## Category #######################


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
    

################## Product ###########################################


class ProductApi(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        camp = Product.objects.all()
        serializer = ProductSerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomPagination(PageNumberPagination):
        page_size = 2  # Number of items per page
        page_size_query_param = 'limit'
        max_page_size = 10  # Maximum number of items per page

class ProductByCategoryApi(APIView):
    def get(self, request, cat_id):
        try:
            # Retrieve data for the specified category
            data = Product.objects.filter(category=cat_id)
            if cat_id is None:
                    return Response({"error": True, "message": "Category ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            data = Product.objects.filter(category=cat_id)
            if not data.exists():
                    return Response({"error": True, "message": "No products found for the given category"}, status=status.HTTP_404_NOT_FOUND)

            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(data, request)
            serializer = ProductSerializer(result_page, many=True)

            return Response(serializer.data)


        except Exception as e:
                return Response({"error": True, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductPutApi(APIView):
    def put(self, request,id):
        try:
            instance = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response({"error" : "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            instance = Product.objects.get(pk=id)
            instance.delete()
            return Response({"message" : "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


#######################  Enquiry #############################3

class BrochureApi(APIView):
    def post(self, request):
        serializer = BrochureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.db import transaction

class ProductBrochureApi(APIView):
    def post(self, request):
        product_serializer = ProductSerializer(data=request.data)
        brochure_serializer = BrochureSerializer(data=request.data)
        if product_serializer.is_valid() and brochure_serializer.is_valid():
            with transaction.atomic():
                product_instance = product_serializer.save()
                brochure_instance = brochure_serializer.save(product=product_instance)
            return Response({
                "product": product_serializer.data,
                "brochure": brochure_serializer.data
            }, status=status.HTTP_201_CREATED)

        else:
            errors = {}
            if not product_serializer.is_valid():
                errors.update(product_serializer.errors)
            if not brochure_serializer.is_valid():
                errors.update(brochure_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


###########################  ProdutItem ##################################
        
class ProductItemApi(APIView):
    def post(self,request):
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        product = ProductItem.objects.all()
        serializer = ProductItemSerializer(product, many=True)
        return Response(serializer.data)
    

class ProductItemPutApi(APIView):
    def put(self, request,id):
        try:
            instance = ProductItem.objects.get(pk=id)
        except ProductItem.DoesNotExist:
            return Response({"error" : "ProductItem not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductItemSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            instance = ProductItem.objects.get(pk=id)
            instance.delete()
            return Response({"message" : "ProductItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ProductItem.DoesNotExist:
            return Response({"error": "ProductItem not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
