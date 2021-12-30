from django.db import models
from accounts.models import User
from .choices import (
    GenderEnum,
    SizeEnum,
    ShoeCharacteristicEnum,
    HairColorEnum,
    EyeColorEnum)


# Create your models here.
class ExtraTailoredSize(models.Model):
    neck = models.CharField(choices=SizeEnum.choices(), max_length=100)
    waist = models.CharField(choices=SizeEnum.choices(), max_length=100)
    bust = models.CharField(choices=SizeEnum.choices(), max_length=100)
    hips = models.CharField(choices=SizeEnum.choices(), max_length=100)
    shoulder = models.CharField(choices=SizeEnum.choices(), max_length=100, blank=True)
    inside_leg = models.CharField(choices=SizeEnum.choices(), max_length=100, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    
class ShoeCharacteristic(models.Model):
    charateristic = models.CharField(choices=ShoeCharacteristicEnum.choices(), max_length=100)
    
    def __str__(self):
        return str(self.charateristic)
    
class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feelings = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=70)
    eye_color = models.CharField(choices=EyeColorEnum.choices(), max_length=100)
    hair_color = models.CharField(choices=HairColorEnum.choices(), max_length=100)
    
    def __str__(self):
        return str(self.user.email)

class InitialProfileDetail(models.Model):
    name = models.CharField(max_length=200)
    profile_name = models.CharField(max_length=200)
    gender = models.CharField(choices=GenderEnum.choices(), max_length=200)
    
    def __str__(self):
        return str(self.name)