from django.urls import path
from .views import *

urlpatterns = [
    path('image',ImageApi.as_view()),   
    path('image/<str:id>',ImageApi.as_view()),

    path('category',CategoryApi.as_view()),
    path('category/<str:id>',CategoryApi.as_view()),

    path('categoryput/<uuid:id>/',CategoryPutApi.as_view()),
    # path('category1',CategoryApi1.as_view()),
    path('categorypagination',CategoryAPIViewPagination.as_view()),
    path('categoryone/<uuid:pk>/', CategoryDetailApi.as_view(), name='category-detail'),
    


]

