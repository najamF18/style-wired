from django.db import models

from accounts.models import User
from men.models import(InitialProfileDetail,
                       PersonalInfo,
                       ExtraTailoredSize)

from men.models import (
    ShoeCharacteristic,
    
                         )

from .choices import (
    SizeEnum,
    FeminineShapeEnum,
    TopStyleEnum,
    HeelHeightEnum,
    ShoeStyleEnum,
    CasualPreferenceEnum,
    WorkPreferenceEnum,
    PrintsEnum,
    ColorsEnum
)
# Create your models here.


    
class WomenSize(models.Model):
    initial_profile_details = models.ForeignKey(InitialProfileDetail, on_delete=models.CASCADE)
    tops = models.CharField(choices=SizeEnum.choices(), max_length=100)
    bottoms = models.CharField(choices=SizeEnum.choices(), max_length=100)
    footwear = models.CharField(choices=SizeEnum.choices(), max_length=100)
    bra = models.CharField(choices=SizeEnum.choices(), max_length=100)
    
    def __str__(self):
        return str(self.initial_profile_details.name)
    
    
class StyleProfileWomen(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    men_size = models.ForeignKey(WomenSize, on_delete=models.CASCADE)
    extra_tailored_sizes = models.ForeignKey(ExtraTailoredSize, on_delete=models.CASCADE)
    feminine_shape = models.CharField(choices=FeminineShapeEnum.choices(), max_length=100)
    top_style = models.CharField(choices=TopStyleEnum.choices(), max_length=100)
    bottom_style = models.CharField(choices=TopStyleEnum.choices(), max_length=100)
    shoe_characterics = models.ManyToManyField(ShoeCharacteristic)
    heel_height = models.CharField(choices=HeelHeightEnum.choices(), max_length=100)
    shoe_style = models.CharField(choices=ShoeStyleEnum.choices(), max_length=100)
    casual_preference = models.CharField(choices=CasualPreferenceEnum.choices(), max_length=100)
    work_preference = models.CharField(choices=WorkPreferenceEnum.choices(), max_length=100)
    prints = models.CharField(choices=PrintsEnum.choices(), max_length=100)
    colors = models.CharField(choices=ColorsEnum.choices(), max_length=100)
    feedback = models.CharField(max_length=500)
    image1 = models.ImageField(blank=True, upload_to='pictures')
    insta_link = models.URLField(blank=True)
    
    def __str__(self):
        return str(self.men_size.initial_profile_details.name)
    

    

    