from django.db import models

from .choices import (
    SpendingRangeEnum,
    AddOnEnum,
    StatusEnum,
    PaymentMethodEnum
)

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Order(models.Model):
    # style_profile = models.ForeignKey(choices=StyleProfileEnum.choices(), on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=999, decimal_places=5)
    status = models.CharField(choices=StatusEnum.choices(), max_length=20)
    payment_method = models.CharField(choices=PaymentMethodEnum.choices(), max_length=20)
    request_date = models.DateField()
    receiving_city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    arrival_date = models.DateField()
    flight_booked = models.BooleanField(default=False)
    flight_number = models.CharField(max_length=100)
    date_to_receive = models.DateField()
    time_to_receive = models.TimeField()
    address = models.CharField(max_length=500)
    # this is how we can confine the genric relation to only allow selective models
    limit = models.Q(app_label = 'men', model = 'styleprofilemen') | models.Q(app_label = 'women', model = 'styleprofilewomen')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    def __str__(self):
        return str(self.content_object.personal_info.user.email)


class Outfit(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ocaasion = models.CharField(max_length=500)
    spending_on_clothing = models.CharField(choices=SpendingRangeEnum.choices(), max_length=50)
    spending_on_shoes = models.CharField(choices=SpendingRangeEnum.choices(), max_length=50)
    spending_on_bag = models.CharField(choices=SpendingRangeEnum.choices(), max_length=50)
    pic = models.ImageField(blank=True)


class AddOn(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    add_on = models.CharField(choices=AddOnEnum.choices(), max_length=20)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    delivery_address = models.CharField(max_length=500)

    
