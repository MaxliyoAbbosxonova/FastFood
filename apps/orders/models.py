from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db.models import Model, ForeignKey, CASCADE, FloatField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, DateTimeField, \
    PositiveIntegerField

from foods.models import Food
from users.models import User, Address
from users.models.addresses import Location


class Order(Model):
    class Status(TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on_the_way'
        DELIVERED = 'DELIVERED', 'delivered'

    user = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    status = CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    total_price = DecimalField(max_digits=10, decimal_places=2, default=0)
    address = ForeignKey(Address, on_delete=CASCADE, related_name='orders', default=0)
    estimated_time = FloatField(default=0)
    created_at = DateTimeField(auto_now_add=True)

    @property
    def calculate(self):
        restaurant = Point(69.2043249, 41.2753321, srid=4326)
        distance = Location.objects.filter(
            pk=self.address.location.id
        ).annotate(distance=Distance('location_point', restaurant)).values_list('distance', flat=True).first()
        return distance.km


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='order_items')
    food = ForeignKey(Food, on_delete=CASCADE, related_name='order_items')
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)
