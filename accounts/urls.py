from django.urls import path
from .views import * 


urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', LoginAPi.as_view()),

]