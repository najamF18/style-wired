from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (
    OrderSerializer,
    AddOnSerializer,
    OutfitSerializer
)
from .models import(
    Order,
    AddOn,
    Outfit
)

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class AddOnView(ListCreateAPIView):
    queryset = AddOn.objects.all()
    serializer_class = AddOnSerializer
    

class AddOnRUDView(RetrieveUpdateDestroyAPIView):
    queryset = AddOn.objects.all()
    serializer_class = AddOnSerializer
    
    
class OutfitView(ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    

class OutfitRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

