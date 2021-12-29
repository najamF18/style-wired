from django.db import models
from .choices import (
    GenderEnum,
    SizeEnum,
    TopFitEnum,
    BottomFitEnum,
    CasualPreferenceEnum,
    WorkPreferenceEnum,
    ShoeTypeEnum,
    NonosEnum,
    ColorsEnum,
    ShoeCharacteristicEnum)
# Create your models here.

class InitialProfileDetail(models.Model):
    name = models.CharField(max_length=200)
    profile_name = models.CharField(max_length=200)
    gender = models.CharField(choices=GenderEnum.choices(), max_length=200)
    
    def __str__(self):
        return str(self.name)
    
class MenSize(models.Model):
    initial_profile_details = models.ForeignKey(InitialProfileDetail, on_delete=models.CASCADE)
    tops = models.CharField(choices=SizeEnum.choices(), max_length=100)
    bottoms = models.CharField(choices=SizeEnum.choices(), max_length=100)
    footwear = models.CharField(choices=SizeEnum.choices(), max_length=100)
    blazer = models.CharField(choices=SizeEnum.choices(), max_length=100)
    formal = models.CharField(choices=SizeEnum.choices(), max_length=100, blank=True)
    
    def __str__(self):
        return str(self.initial_profile_details.name)
    
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
    
    
class StyleProfileMen(models.Model):
    men_size = models.ForeignKey(MenSize, on_delete=models.CASCADE)
    work_preferrence = models.CharField(choices=WorkPreferenceEnum.choices(), max_length=100)
    casual_preferrence = models.CharField(choices=CasualPreferenceEnum.choices(), max_length=100)
    topfit = models.CharField(choices=TopFitEnum.choices(), max_length=100)
    bottomfit = models.CharField(choices=BottomFitEnum.choices(), max_length=100)
    shoe_characterics = models.ManyToManyField(ShoeCharacteristic)
    shoe_type = models.CharField(choices=ShoeTypeEnum.choices(), max_length=100)
    no_nos = models.CharField(choices=NonosEnum.choices(), max_length=100)
    colors = models.CharField(choices=ColorsEnum.choices(), max_length=100)
    feedback = models.CharField(max_length=500)
    image1 = models.ImageField(blank=True, upload_to='pictures')
    insta_link = models.URLField(blank=True)
    
    def __str__(self):
        return str(self.men_size.initial_profile_details.name)
    

    