from django.urls import path

from orders.views import OrderListApiView, OrderDetailApiView, UserOrdersListApiView, OrderCreateAPIView, \
    OrderItemListApiView

urlpatterns = [path('', OrderListApiView.as_view(), name='orders'),
               path('orders/<int:pk>/', OrderDetailApiView.as_view(), name='order'),
               path('user/orders/', UserOrdersListApiView.as_view(), name='order_a'),

               path('create/', OrderCreateAPIView.as_view(), name='order_create'),
               path('orderitems/', OrderItemListApiView.as_view(), name='order_items'),
               ]
