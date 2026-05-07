from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, IntegerField, TextField, DateTimeField
from users.models import User
from foods.models import Food

class Order(Model):
    class Status(TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on_the_way'
        DELIVERED = 'DELIVERED', 'delivered'

    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    status=CharField(choices=Status.choices, default=Status.PENDING, max_length=10)
    total_price = DecimalField(max_digits=10, decimal_places=2)
    delivery_address = TextField(max_length=500, null=True, blank=True)
    latitude = DecimalField(max_digits=9, decimal_places=7)
    longitude = DecimalField(max_digits=9, decimal_places=7)
    estimated_time = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    food = ForeignKey(Food, on_delete=CASCADE)
    quantity = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
