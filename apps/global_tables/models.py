from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, CharField
from django.db.models.fields import FloatField
from rest_framework.fields import IntegerField

from restaurants.models import Restaurants
from orders.models import Order


# Create your models here.


class GlobalOrder(models.Model):
    tenant = CharField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_time = FloatField(default=0)
