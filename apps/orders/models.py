from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, IntegerField, TextField, DateTimeField, \
    PositiveIntegerField
from users.models import User
from foods.models import Food

class Order(Model):
    class Status(TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on_the_way'
        DELIVERED = 'DELIVERED', 'delivered'

    user = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    status=CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    total_price = DecimalField(max_digits=10, decimal_places=2)
    delivery_address = TextField(max_length=500, null=True, blank=True)
    latitude = DecimalField(max_digits=9, decimal_places=7)
    longitude = DecimalField(max_digits=9, decimal_places=7)
    estimated_time = DateTimeField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    food = ForeignKey(Food, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)
