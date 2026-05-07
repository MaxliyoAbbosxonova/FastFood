from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone')
        write_only_fields = ('id', 'password')
