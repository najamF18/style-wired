from django.db.models import fields
from rest_framework import serializers
from .models import(
    WomenSize,
    StyleProfileWomen,
)
        
class WomenSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WomenSize
        fields = '__all__'
        
        
class StyleProfileWomenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StyleProfileWomen
        fields = '__all__'
        
