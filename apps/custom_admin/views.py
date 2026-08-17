# Create your views here.
from django.db.models import Sum, Avg
from django.utils import timezone

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from global_tables.models import GlobalOrder
from orders.models import Order
from restaurants.models import Restaurants


def load_page(request, page):
    return render(request, f"custom_admin/{page}.html")

def base(request):
    return render(request, 'custom_admin/base.html')

def login(request):
    return render(request,'custom_admin/login.html')

def dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

class DashboardAPIView(APIView):
    def get(self, request):
        today=timezone.now().date()
        total_revenue= GlobalOrder.objects.aggregate(total=Sum("total_price"))["total"] or 0
        avg_revenue= round(GlobalOrder.objects.aggregate(total=Avg("total_price"))["total"] or 0)
        avg_time= round(GlobalOrder.objects.aggregate(total=Avg("estimated_time"))["total"] or 0)
        today_revenue=GlobalOrder.objects.filter(created_at__date=today).aggregate(total=Sum("total_price"))["total"] or 0
        return Response({
            "total_orders": GlobalOrder.objects.count(),
            "total_res": Restaurants.objects.filter(is_active=True).count(),
            "total_orders_today":GlobalOrder.objects.filter(created_at__date=today).count(),
            "total_revenue":total_revenue,
            "today_revenue":today_revenue,
            "avg_revenue":avg_revenue,
            "avg_time":avg_time,        })

def analytics(request):
    return render(request, "custom_admin/analytics.html")


def orders(request):
    return render(request, "custom_admin/orders.html")


def restaurants(request):
    return render(request, "custom_admin/restaurants.html")


def couriers(request):
    return render(request, "custom_admin/couriers.html")


def customers(request):
    return render(request, "custom_admin/customers.html")


def live_monitor(request):
    return render(request, "custom_admin/live_monitor.html")


def maps_geo(request):
    return render(request, "custom_admin/maps_geo.html")


def ai_insights(request):
    return render(request, "custom_admin/ai_insights.html")


def finance(request):
    return render(request, "custom_admin/finance.html")


def reports(request):
    return render(request, "custom_admin/reports.html")


def promotions(request):
    return render(request, "custom_admin/promotions.html")


def reviews(request):
    return render(request, "custom_admin/reviews.html")


def notifications(request):
    return render(request, "custom_admin/notifications.html")


def settings(request):
    return render(request, "custom_admin/settings.html")

def management(request):
    return render(request, "custom_admin/management.html")

def permissions(request):
    return render(request, "custom_admin/permissions.html")
