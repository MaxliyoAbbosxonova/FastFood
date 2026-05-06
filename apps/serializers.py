from rest_framework.serializers import ModelSerializer

from apps.models import User, Food, Order, OrderItem, Category


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone')
        write_only_fields = ('id', 'password')



class FoodModelSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

