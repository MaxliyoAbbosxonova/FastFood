from django.utils import timezone
from rest_framework.serializers import ModelSerializer

from global_tables.models import GlobalOrder
from orders.models import Order, OrderItem


class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    order_items = OrderItemModelSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderListModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'status', 'created_at']


class OrderItemCreateSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food', 'quantity']


class OrderCreateSerializer(ModelSerializer):
    order_items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['address', 'order_items']

    def create(self, validated_data):
        items = validated_data.pop('order_items')

        order = Order.objects.create(
            user=self.context['request'].user, **validated_data)
        total = 0

        for item in items:
            food = item['food']
            quantity = item['quantity']

            order_item = OrderItem.objects.create(
                order=order,
                food=food,
                quantity=quantity,
                price=food.price * quantity
            )

            total += order_item.price
        request = self.context['request']
        order.total_price = total
        order.save()
        time=order.calculate
        order.estimated_time = time
        order.save(update_fields=["estimated_time"])

        GlobalOrder.objects.create(
            tenant=request.tenant.schema_name,
            total_price=total,
            status="PENDING",
            created_at=timezone.now(),
            estimated_time=time,
        )
        return order
