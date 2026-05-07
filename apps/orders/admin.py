from django.contrib import admin
from django.contrib.admin import ModelAdmin

from orders.models import Order, OrderItem


# Register your models here.

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('user', 'name', 'total_price', 'delivery_address', 'created_at')
    search_fields = ('name', 'id')


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ('order', 'food', 'quantity', 'price')
