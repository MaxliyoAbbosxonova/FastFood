from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from global_tables.models import GlobalOrder
from global_tables.serializers import GlobalModelSerializer

# Create your views here.


class GlobalOrderListCreateApiView(ListCreateAPIView):
    queryset = GlobalOrder.objects.all()
    serializer_class = GlobalModelSerializer
