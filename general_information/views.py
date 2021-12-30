from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (
    InitialProfileDetailSerializer,
    ShoeCharacteristicSerializer,
    ExtraTailoredSizeSerializer,
    PersonalInfoSerializer
)
from .models import(
    InitialProfileDetail,
    ExtraTailoredSize,
    ShoeCharacteristic,
    PersonalInfo
)

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class InitialProfileDetailView(ListCreateAPIView):
    queryset = InitialProfileDetail.objects.all()
    serializer_class = InitialProfileDetailSerializer
    

class InitialProfileDetailRUDView(RetrieveUpdateDestroyAPIView):
    queryset = InitialProfileDetail.objects.all()
    serializer_class = InitialProfileDetailSerializer
    
    
class ExtraTailoredSizeView(ListCreateAPIView):
    queryset = ExtraTailoredSize.objects.all()
    serializer_class = ExtraTailoredSizeSerializer
    

class ExtraTailoredSizeRUDView(RetrieveUpdateDestroyAPIView):
    queryset = ExtraTailoredSize.objects.all()
    serializer_class = ExtraTailoredSizeSerializer
    
    
class ShoeCharacteristicView(ListCreateAPIView):
    queryset = ShoeCharacteristic.objects.all()
    serializer_class = ShoeCharacteristicSerializer
    

class ShoeCharacteristicRUDView(RetrieveUpdateDestroyAPIView):
    queryset = ShoeCharacteristic.objects.all()
    serializer_class = ShoeCharacteristicSerializer
    
    

class PersonalInfoView(ListCreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    

class PersonalInfoRUDView(RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

