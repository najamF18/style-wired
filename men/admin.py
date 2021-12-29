from django.contrib import admin
from .models import (
    InitialProfileDetail,
    MenSize,
    ExtraTailoredSize,
    StyleProfileMen,
    ShoeCharacteristic)
# Register your models here.

admin.site.register(InitialProfileDetail)
admin.site.register(MenSize)
admin.site.register(ExtraTailoredSize)
admin.site.register(StyleProfileMen)
admin.site.register(ShoeCharacteristic)
