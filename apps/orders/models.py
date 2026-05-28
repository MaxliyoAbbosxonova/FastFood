from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, IntegerField, DateTimeField, \
    PositiveIntegerField

from shared import utils
from users.models import User, Address
from foods.models import Food
from math import ceil
from django.db.models import Sum


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
    estimated_time = IntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)

    @property
    def calculate_estimated_time(self):
        restaurant_lat = 41.2753321
        restaurant_lon = 69.2043249
        distance = utils.haversine(
            restaurant_lat,
            restaurant_lon,
            float(self.address.latitude),
            float(self.address.longitude)
        )
        total_foods = self.order_items.aggregate(total=Sum('quantity'))['total'] or 0

        prep_time = ceil(total_foods / 4) * 5
        delivery_time = distance * 3

        return round(prep_time + delivery_time)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='order_items')
    food = ForeignKey(Food, on_delete=CASCADE, related_name='order_items')
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)
