from django.db.models import fields
from rest_framework import serializers
from .models import(
    InitialProfileDetail,
    ExtraTailoredSize,
    ShoeCharacteristic,
    PersonalInfo
)

class InitialProfileDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InitialProfileDetail
        fields = '__all__'
        

class ExtraTailoredSizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExtraTailoredSize
        fields = '__all__'
        
    
class ShoeCharacteristicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShoeCharacteristic
        fields = '__all__'
        

class PersonalInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalInfo
        fields = '__all__'