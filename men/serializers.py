from django.db.models import fields
from rest_framework import serializers
from .models import(
    MenSize,
    StyleProfileMen,
)
        
class MenSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenSize
        fields = '__all__'
        
        
class StyleProfileMenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StyleProfileMen
        fields = '__all__'
        
