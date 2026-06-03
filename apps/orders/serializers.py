from rest_framework.serializers import ModelSerializer

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

        order.total_price = total
        order.estimated_time = order.calculate
        order.save()

        return order
