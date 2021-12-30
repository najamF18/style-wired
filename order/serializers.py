from django.db.models import fields
from rest_framework import serializers
from .models import(
    Order,
    AddOn,
    Outfit
)
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        
        
class AddOnSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddOn
        fields = '__all__'
        

class OutfitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Outfit
        fields = '__all__'
        
