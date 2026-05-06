from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from apps.models import Food, Order, Category
from apps.permissions import Is_Waiter
from apps.serializers import FoodModelSerializer, OrderModelSerializer, CategoryModelSerializer


# Create your views here.


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


class OrdersListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAdminUser, Is_Waiter]


class OrderCreateApiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAuthenticated]


class OrderDetailApiView(APIView):

    def patch(self, request, pk):
        if request.user.role == 'ADMIN' and request.user.role == 'WAITER':
            try:
                order = Order.objects.get(id=pk)
            except Order.DoesNotExist:
                return Response({"error": "Order topilmadi"}, status=404)

            new_status = request.data.get("status")

            if not new_status:
                return Response({"error": "Status berilmadi"}, status=400)

            order.status = new_status
            order.save()

            return Response({
                "message": "Status yangilandi",
                "status": order.status
            }, status=200)


class OrderDetailAdminApiView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAdminUser]


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [AllowAny]


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]
