from rest_framework.serializers import ModelSerializer

from restaurants.models import RestaurantsCategory,Restaurants


class ResCategoryModelSerializers(ModelSerializer):
    class Meta:
        model=RestaurantsCategory
        fields='__all__'

class RestaurantsModelSerializers(ModelSerializer):
    class Meta:
        model=Restaurants
        fields='__all__'

