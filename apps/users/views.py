from django.db.migrations import serializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from shared.utils import random_code, send_sms_code
from .models import User, Address
from .serializers import UserModelSerializer, AddressModelSerializer, SendSmsCodeSerializer, \
    RegisterModelSerializer, CheckSmsCodeSerializer, LoginSerializer


@extend_schema(tags=['User'])
class AddressListAPIView(ListAPIView):
    serializer_class = AddressModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.role == 'ADMIN':
            return Address.objects.all()
        elif self.request.user.is_authenticated:
            return Address.objects.filter(user=self.request.user)


@extend_schema(tags=["User"])
class AddressCreateAPIView(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["User"])
class AddressDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['User'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]


class RegisterApiView(APIView):
    serializer_class = RegisterModelSerializer
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })


class CheckSmsCodeAPIView(APIView):
    serializer_class = CheckSmsCodeSerializer
    authentication_classes = ()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.get_data)


@extend_schema(tags=["User"])
class SendCodeApiView(APIView):
    serializer_class = SendSmsCodeSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = random_code()
        phone = serializer.validated_data['phone']
        result = send_sms_code(phone, code)
        if not result["allowed"]:
            return Response({
                "message": f"{result['remain_seconds']} sekunddan so'ng yubora olasiz."
            }, status=429)

        return Response({"message": "Send sms code"})


@extend_schema(tags=["User"])
class AdminLoginApiView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.get_data)
