from django.urls import path
from.views import *


urlpatterns = [
    path('product',ProductApi.as_view()),
    
    path('productbycategory/<uuid:id>/', ProductByCategoryApi.as_view(), name='category-detail'),
    path('productput/<uuid:id>/', ProductPutApi.as_view(), name='category-detail'),
    path('productpagination',ProductPagination.as_view()),
    path('productlist/',ProductListAPI.as_view()),
    
    path('productitem',ProductItemApi.as_view()),
    path('productitembrochure', ProductItemBrochureApi.as_view()),

    path('getbrochurepath/<uuid:id>', GetBrochureApi.as_view()),

    path('productitemput/<uuid:id>/', ProductItemPutApi.as_view(), name='product'),
    path('productitembyproduct/<str:product_id>/', ProductItemByProduct.as_view(), name='productitem-detail'),

    path('productitems/<str:title>/', ProductItemByTitle.as_view(),),
    
    path('productbrochure',ProductBrochureApi.as_view()),
    path('product-id/<uuid:id>/',ProductByIDApi.as_view()),

    
]