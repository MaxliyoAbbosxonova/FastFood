from django.urls import path, include

urlpatterns = [
    path('',include('foods.urls')),
    path('users/',include('users.urls')),
    path('orders/',include('orders.urls')),
]