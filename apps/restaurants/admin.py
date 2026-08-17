from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_tenants.admin import TenantAdminMixin

from restaurants.models import Restaurants, RestaurantsCategory, Domain


# Register your models here.

@admin.register(Restaurants)
class RestaurantsAdmin(TenantAdminMixin,ModelAdmin):
    list_display = ('id','name','description','phone','email','is_active','is_open')

@admin.register(RestaurantsCategory)
class ResCategoryAdmin(ModelAdmin):
    list_display = ('id','name','icon')

@admin.register(Domain)
class DomainAdmin(ModelAdmin):
    list_display = ('domain',)