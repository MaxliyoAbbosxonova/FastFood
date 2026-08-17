import math
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db import connection
from django.db.models import Model, ForeignKey, CASCADE, FloatField, Sum
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, DateTimeField, \
    PositiveIntegerField

from foods.models import Food
from restaurants.models import Restaurants
from users.models import User, Address
from users.models.addresses import Location


class Order(Model):
    class Status(TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on_the_way'
        DELIVERED = 'DELIVERED', 'delivered'
        CANCELLED='CANCELLED','cancelled'

    user = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    status = CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    total_price = DecimalField(max_digits=10, decimal_places=2, default=0)
    address = ForeignKey(Address, on_delete=CASCADE, related_name='orders', default=0)
    estimated_time = FloatField(default=0)
    created_at = DateTimeField(auto_now_add=True)

    @property
    def current_restaurant(self):
        return Restaurants.objects.only("location_point").get(
            schema_name=connection.schema_name
        )

    @property
    def calculate(self):
        distance = Location.objects.filter(pk=self.address.location.id).annotate(
            distance=Distance(
                "location_point",
                self.current_restaurant.location_point
            )).values_list('distance', flat=True).first()


        total_quantity = self.order_items.aggregate(
            total=Sum("quantity")
        )["total"] or 0

        preparation_time = math.ceil(total_quantity / 4) * 5

        return distance.km*3+preparation_time


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='order_items')
    food = ForeignKey(Food, on_delete=CASCADE, related_name='order_items')
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)
