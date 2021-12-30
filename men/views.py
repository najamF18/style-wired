from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (
    StyleProfileMenSerializer,
    MenSizeSerializer,
)
from .models import(
    MenSize,
    StyleProfileMen,
)

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class MenSizeView(ListCreateAPIView):
    queryset = MenSize.objects.all()
    serializer_class = MenSizeSerializer
    

class MenSizeRUDView(RetrieveUpdateDestroyAPIView):
    queryset = MenSize.objects.all()
    serializer_class = MenSizeSerializer
    
    
class StyleProfileMenView(ListCreateAPIView):
    queryset = StyleProfileMen.objects.all()
    serializer_class = StyleProfileMenSerializer
    

class StyleProfileMenRUDView(RetrieveUpdateDestroyAPIView):
    queryset = StyleProfileMen.objects.all()
    serializer_class = StyleProfileMenSerializer

