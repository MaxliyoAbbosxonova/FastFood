from django.urls import path

from foods.views import FoodsListApiView, FoodDetailApiView, FoodCreateApiView, CategoryListApiView, \
    CategoryCreateApiView

urlpatterns = [
    path('foods/', FoodsListApiView.as_view(), name='foods'),
    path('foods/<int:pk>/', FoodDetailApiView.as_view(), name='food'),
    path('foods/create/', FoodCreateApiView.as_view(), name='food'),
    path('categories/', CategoryListApiView.as_view(), name='food'),
    path('categories/create/', CategoryCreateApiView.as_view(), name='food'),
]