from django.contrib import admin
from .models import (
    Order,
    Outfit,
    AddOn
)
# Register your models here.

admin.site.register(Outfit)
admin.site.register(Order)
admin.site.register(AddOn)
