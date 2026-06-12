
from django.urls import path

from custom_admin.views import dashboard

urlpatterns=[
    path('',dashboard,name='custom_dashboard')
]