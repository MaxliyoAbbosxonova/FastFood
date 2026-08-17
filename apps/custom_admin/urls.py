from django.urls import path

from custom_admin.views import base, dashboard, analytics, orders, restaurants, couriers, customers, live_monitor, \
    maps_geo, ai_insights, finance, reports, promotions, reviews, notifications, settings, management, permissions, \
    load_page, DashboardAPIView, login

urlpatterns = [


    path('base/', base, name='custom_admin_bar'),
    path('', login, name='custom_login'),

    path('cards/',DashboardAPIView.as_view()),
    path('dashboard/', dashboard, name='dashboard'),
    path('analytics/', analytics, name='analytics'),
    path('orders/', orders, name='orders'),
    path('restaurants/', restaurants, name='restaurants'),
    path('couriers/', couriers, name='couriers'),
    path('customers/', customers, name='customers'),
    path('live_monitor/', live_monitor, name='live_monitor'),
    path('maps_geo/', maps_geo, name='maps_geo'),
    path('ai_insights/', ai_insights, name='ai_insights'),
    path('finance/', finance, name='finance'),
    path('reports/', reports, name='reports'),
    path('management/', management, name='management'),
    path('promotions/', promotions, name='promotions'),
    path('reviews/', reviews, name='reviews'),
    path('notifications/', notifications, name='notifications'),
    path('settings/', settings, name='settings'),
    path('permissions/', permissions, name='permissions'),
    path("<str:page>/", load_page),

]
