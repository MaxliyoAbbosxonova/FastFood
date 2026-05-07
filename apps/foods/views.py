# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from foods.models import Food, Category
from permissions import Is_Waiter
from foods.serializers import FoodModelSerializer, CategoryModelSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [AllowAny]


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]


class FoodsListApiView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [AllowAny]


class FoodCreateApiView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [IsAdminUser, Is_Waiter]


class FoodDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [IsAdminUser, Is_Waiter]
