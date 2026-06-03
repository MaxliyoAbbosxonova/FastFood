import re

from django.core.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.tokens import RefreshToken

from shared.utils import check_sms_code
from .models import User, Address


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class RegisterModelSerializer(ModelSerializer):
    token_class = RefreshToken

    class Meta:
        model = User
        fields = ('phone', 'full_name', 'password')
        write_only_fields = ('password',)

    def validate(self, attrs):
        phone = attrs['phone']

        if User.objects.filter(phone=phone).exists():
            raise ValidationError({
                "phone": "Bu telefon raqam ro'yxatdan o'tgan"
            })

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


# Send sms code Done

class SendSmsCodeSerializer(ModelSerializer):
    phone = CharField(default='933977090')

    def validate_phone(self, value):
        digits = re.findall(r'\d', value)
        if len(digits) < 9:
            raise ValidationError('Phone number must be at least 9 digits')
        phone = ''.join(digits)
        return phone.removeprefix('998')

    class Meta:
        model = User
        fields = ['phone']


class CheckSmsCodeSerializer(Serializer):
    phone = CharField()
    code = IntegerField()
    token_class = RefreshToken

    def validate_phone(self, value):
        digits = re.findall(r'\d', value)
        if len(digits) < 9:
            raise ValidationError('Phone number must be at least 9 digits')
        phone = ''.join(digits)
        return phone.removeprefix('998')

    def validate(self, validated_data):
        phone = validated_data.get('phone')
        code = validated_data.get('code')

        if not check_sms_code(phone, code):
            raise ValidationError('Invalid code')

        self.user = User.objects.filter(phone=validated_data['phone']).first()
        if not self.user:
            raise ValidationError('Code entered correct but user is not registered ')
        return validated_data

    @property
    def get_data(self):
        refresh = self.get_token(self.user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)
