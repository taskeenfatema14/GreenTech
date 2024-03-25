from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator
import math
from rest_framework.pagination import PageNumberPagination
from django.db import transaction


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
        serializer = ProductSerializer1(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomPagination(PageNumberPagination):
        page_size = 2  # Number of items per page
        page_size_query_param = 'limit'
        max_page_size = 10  # Maximum number of items per page

class ProductByCategoryApi(APIView):
    def get(self, request, id):
        try:
            # Retrieve data for the specified category
            data = Product.objects.filter(id=id)
            if id is None:
                    return Response({"error": True, "message": "Category ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            data = Product.objects.filter(id=id)
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
        
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductPagination(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 6)  # Number of items per page
        
        page = request.GET.get('page')
        try:
            paginated_products = paginator.page(page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)
        
        serializer = ProductSerializer(paginated_products, many=True)
        
        return Response({
            'products': serializer.data
        }, status=status.HTTP_200_OK)

class ProductListAPI(APIView):
    def get(self, request):    
        data = Product.objects.all()
        serializer = ProductListSerilaizer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class ProductItemByProduct(APIView):
    def get(self, request, product_id, format=None):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductItemByTitle(APIView):
    def get(self, request, title, format=None):
        try:
            product = Product.objects.get(title=title)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product_items = ProductItem.objects.filter(product=product)
        serializer = ProductItemSerializer(product_items, many=True)
        return Response(serializer.data)


#######################  Enquiry #############################3

class BrochureApi(APIView):
    def post(self, request):
        serializer = BrochureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Working for Seperately passing brochure and product
class ProductBrochureApi(APIView):
    def post(self, request):
        product_serializer = ProductItemSerializer(data=request.data.get('product'))
        brochure_serializer = BrochureSerializer(data=request.data.get('brochure'))
        if product_serializer.is_valid() and brochure_serializer.is_valid():
            with transaction.atomic():
                product_instance = product_serializer.save()
                # Ensure correct field name for the relationship
                brochure_instance = brochure_serializer.save(productitem=product_instance)
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