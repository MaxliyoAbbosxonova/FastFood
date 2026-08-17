from django.urls import path

from global_tables.views import GlobalOrderListCreateApiView

urlpatterns=[
    path('',GlobalOrderListCreateApiView.as_view())
]