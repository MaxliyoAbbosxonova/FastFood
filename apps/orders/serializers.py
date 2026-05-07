from rest_framework.serializers import ModelSerializer

from orders.models import Order, OrderItem


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
#
