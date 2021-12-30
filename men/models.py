from django.db import models
from general_information.models import (
    PersonalInfo,
    InitialProfileDetail,
    ExtraTailoredSize,
    ShoeCharacteristic
)

from .choices import (
    SizeEnum,
    TopFitEnum,
    BottomFitEnum,
    CasualPreferenceEnum,
    WorkPreferenceEnum,
    ShoeTypeEnum,
    NonosEnum,
    ColorsEnum,)


# Create your models here.
    
class MenSize(models.Model):
    initial_profile_details = models.ForeignKey(InitialProfileDetail, on_delete=models.CASCADE)
    tops = models.CharField(choices=SizeEnum.choices(), max_length=100)
    bottoms = models.CharField(choices=SizeEnum.choices(), max_length=100)
    footwear = models.CharField(choices=SizeEnum.choices(), max_length=100)
    blazer = models.CharField(choices=SizeEnum.choices(), max_length=100)
    formal = models.CharField(choices=SizeEnum.choices(), max_length=100, blank=True)
    
    def __str__(self):
        return str(self.initial_profile_details.name)
    
    
class StyleProfileMen(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    men_size = models.ForeignKey(MenSize, on_delete=models.CASCADE)
    extra_tailored_sizes = models.ForeignKey(ExtraTailoredSize, on_delete=models.CASCADE)
    work_preference = models.CharField(choices=WorkPreferenceEnum.choices(), max_length=100)
    casual_preference = models.CharField(choices=CasualPreferenceEnum.choices(), max_length=100)
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
    

    

    