from django.urls import path

from orders.views import OrdersListApiView, OrderDetailApiView, OrderDetailAdminApiView

urlpatterns=[path('orders/',OrdersListApiView.as_view(),name='orders'),
    path('order/<int:pk>/',OrderDetailApiView.as_view(),name='order'),
    path('order_a/<int:pk>',OrderDetailAdminApiView.as_view(),name='order_a'),

]