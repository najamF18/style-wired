from django.db.models import fields
from rest_framework import serializers
from .models import(
    InitialProfileDetail,
    MenSize,
    ExtraTailoredSize,
    ShoeCharacteristic,
    StyleProfileMen
)

class InitialProfileDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InitialProfileDetail
        fields = '__all__'
        

        
class MenSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenSize
        fields = '__all__'
        

class ExtraTailoredSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExtraTailoredSize
        fields = '__all__'
        
    
class ShoeCharacteristicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShoeCharacteristic
        fields = '__all__'
        
        
class StyleProfileMenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StyleProfileMen
        fields = '__all__'