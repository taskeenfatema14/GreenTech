from django.urls import path
from .views import *

urlpatterns = [
    path('image',ImageApi.as_view()),    
    path('category',CategoryApi.as_view()),
    path('GetOneImageApi',GetOneImageApi.as_view()),

]

