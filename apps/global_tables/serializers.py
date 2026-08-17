from rest_framework.serializers import ModelSerializer

from global_tables.models import GlobalOrder


class GlobalModelSerializer(ModelSerializer):
    class Meta:
        model=GlobalOrder
        fields=('tenant','total_price','status','created_at','estimated_time')


