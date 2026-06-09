from django.urls import path

from restaurants.views import ResCategoryListCreateAPIView, ResCategoryRetrieveUpdateDelete, \
    RestaurantsListCreateAPIView, RestaurantsRetrieveUpdateDestroyAPIView

urlpatterns=[
    path('res-category/',ResCategoryListCreateAPIView.as_view()),
    path('res-category/<int:pk>',ResCategoryRetrieveUpdateDelete.as_view()),
    path('',RestaurantsListCreateAPIView.as_view()),
    path('<int:pk>',RestaurantsRetrieveUpdateDestroyAPIView.as_view())
]