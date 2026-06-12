from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from restaurants.models import RestaurantsCategory,Restaurants
from restaurants.serializers import ResCategoryModelSerializers, RestaurantsModelSerializers


# Create your views here.


class ResCategoryListCreateAPIView(ListCreateAPIView):
    queryset = RestaurantsCategory.objects.all()
    serializer_class = ResCategoryModelSerializers
    permission_classes = []

class ResCategoryRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantsCategory.objects.all()
    serializer_class = ResCategoryModelSerializers
    permission_classes = []

class RestaurantsListCreateAPIView(ListCreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsModelSerializers
    permission_classes = []

class RestaurantsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsModelSerializers
    permission_classes = []