from django.urls import path
from .views import *

urlpatterns = [
    path('image',ImageApi.as_view()),   
    path('GetOneImageApi',GetOneImageApi.as_view()),

    path('category',CategoryApi.as_view()),
    path('categoryput/<uuid:id>/',CategoryPutApi.as_view()),
    # path('category1',CategoryApi1.as_view()),
    path('category123',CategoryAPIViewPagination.as_view()),
    path('categoryone/<uuid:pk>/', CategoryDetailApi.as_view(), name='category-detail'),
    
    path('product',ProductApi.as_view()),
    path('productbycategory/<uuid:cat_id>/', ProductByCategoryApi.as_view(), name='category-detail'),
    path('productput/<uuid:id>/', ProductPutApi.as_view(), name='category-detail'),
    
    path('productitem',ProductItemApi.as_view()),
    path('productitemput/<uuid:id>/', ProductItemPutApi.as_view(), name='category-detail'),


    path('brochure',BrochureApi.as_view()),
    path('productbrochure',ProductBrochureApi.as_view()),


]

