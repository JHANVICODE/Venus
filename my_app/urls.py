from django.urls import path
from .views import *

urlpatterns = [
    path('ping/',ping,name='ping'),
    path('student/',StudentApi.as_view()),
    path('student/<int:pk>/',StudentApi.as_view()),
  
]