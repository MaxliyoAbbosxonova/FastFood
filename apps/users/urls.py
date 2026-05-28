from django.urls import path

from users.views import UserListAPIView, AddressListAPIView, AddressDetailAPIView, AddressCreateAPIView, \
    LoginApiView, SendCodeApiView, RegisterApiView

urlpatterns=[
path('',UserListAPIView.as_view()),
    path('address/',AddressListAPIView.as_view()),
    path('address/<int:pk>',AddressDetailAPIView.as_view()),
    path('address/create/',AddressCreateAPIView.as_view()),
    path("login/",LoginApiView.as_view()),
    path('send_sms/',SendCodeApiView.as_view()),
    path("register/",RegisterApiView.as_view()),

]