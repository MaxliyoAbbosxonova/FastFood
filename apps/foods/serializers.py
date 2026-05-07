from rest_framework.serializers import ModelSerializer

from foods.models import  Food,  Category


class FoodModelSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

