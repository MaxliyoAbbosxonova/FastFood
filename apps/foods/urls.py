from django.urls import path

from foods.views import FoodsListApiView, FoodDetailApiView

urlpatterns = [
    path('foods/', FoodsListApiView.as_view(), name='foods'),
    path('foods/<int:pk>/', FoodDetailApiView.as_view(), name='food'),
]