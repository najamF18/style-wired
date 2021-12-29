from rest_framework import serializers
from .models import(
    User,
)

class UserSerializer(serializers.ModelSerializer):
    
    confirmPassword = serializers.CharField(max_length=200, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'confirmPassword', 'name', 'phone', 'profile_photo')
        write_only_fields = ['confirmPassword']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
        
    def validate(self, attrs):
            if attrs['confirmPassword'] == attrs['password']:
                del attrs['confirmPassword']
                return super().validate(attrs)
            else:
                raise serializers.ValidationError("passwords did not match")    
        
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        # hashing the password for security
        user.set_password(user.password)
        user.save()
        return user
