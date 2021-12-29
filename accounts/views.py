from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class check(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("in get")
        return HttpResponse("hi")

class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

