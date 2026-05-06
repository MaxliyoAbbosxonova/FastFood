from django.urls import path

from apps.views import FoodsListApiView, FoodDetailApiView, OrdersListApiView, OrderDetailApiView, \
    OrderDetailAdminApiView

urlpatterns=[
    path('foods/',FoodsListApiView.as_view(),name='foods'),
    path('foods/<int:pk>/',FoodDetailApiView.as_view(),name='food'),
    path('orders/',OrdersListApiView.as_view(),name='orders'),
    path('order_w/<int:pk>/',OrderDetailApiView.as_view(),name='order'),
    path('order/<int:pk>',OrderDetailAdminApiView.as_view(),name='order'),



]