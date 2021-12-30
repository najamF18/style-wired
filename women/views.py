from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (
    StyleProfileWomenSerializer,
    WomenSizeSerializer,
)
from .models import(
    WomenSize,
    StyleProfileWomen,
)

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class WomenSizeView(ListCreateAPIView):
    queryset = WomenSize.objects.all()
    serializer_class = WomenSizeSerializer
    

class WomenSizeRUDView(RetrieveUpdateDestroyAPIView):
    queryset = WomenSize.objects.all()
    serializer_class = WomenSizeSerializer
    
    
class StyleProfileWomenView(ListCreateAPIView):
    queryset = StyleProfileWomen.objects.all()
    serializer_class = StyleProfileWomenSerializer
    

class StyleProfileWomenRUDView(RetrieveUpdateDestroyAPIView):
    queryset = StyleProfileWomen.objects.all()
    serializer_class = StyleProfileWomenSerializer

