from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from math import sqrt, asin,cos,pi
from orders.models import Order, OrderItem


class OrderModelSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

