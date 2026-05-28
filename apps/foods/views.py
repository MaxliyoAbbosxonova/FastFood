# Create your views here.
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from foods.models import Food, Category
from shared.permissions import IsWaiter
from foods.serializers import FoodModelSerializer, CategoryModelSerializer

@extend_schema(tags=['Food'])
class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Food'])
class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Food'])
class FoodsListApiView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Food'])
class FoodCreateApiView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [IsAdminUser, IsWaiter]

@extend_schema(tags=['Food'])
class FoodDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [IsAdminUser, IsWaiter]
