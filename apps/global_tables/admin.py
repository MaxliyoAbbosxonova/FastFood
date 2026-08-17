from django.contrib import admin
from django.contrib.admin import ModelAdmin

from global_tables.models import GlobalOrder


# Register your models here.


@admin.register(GlobalOrder)
class GlobalAdmin(ModelAdmin):
    list_display = ('tenant','total_price','created_at','estimated_time')