from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from orders.models import Order
from orders.serializers import OrderListModelSerializer, OrderModelSerializer, OrderCreateSerializer
from shared.permissions import IsWaiter, IsAdminOrWaiter


# Create your views here.

@extend_schema(tags=['Order'])
class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAdminOrWaiter]


@extend_schema(tags=['Order'])
class UserOrdersListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


@extend_schema(tags=['Order'])
class OrderDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = [IsAdminOrWaiter]


@extend_schema(tags=['Order'])
class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['Order'])
class OrderItemListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListModelSerializer
    permission_classes = [IsAdminUser]

# class OrdersListApiView(ListCreateAPIView):
#     queryset = Order.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderModelSerializer
#
#     def get_serializer_class(self):
#         if self.request.user.role == 'USER' and self.request.user.method == 'GET':
#             return OrderListModelSerializer
#         else:
#             return OrderModelSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         if self.request.user.role == 'USER':
#             return qs.filter(order__user=self.request.user)
#         elif self.request.user.role == 'ADMIN' or self.request.user.role == 'Waiter':
#             return qs.all()

#
# class OrderItemListApiView(ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderListModelSerializer
#     permission_classes = [IsAdminUser]
#     def get_permissions(self):
#         if self.request.method == "PATCH" or self.request.method == 'GET':
#             self.permission_classes = [IsWaiter, IsAdminUser]
#
