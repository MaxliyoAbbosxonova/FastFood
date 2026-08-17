from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from .models import User, Address


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id','full_name', "phone",'role', "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    ordering = ("phone",)

    fieldsets = (
        (None, {"fields": ("phone", "password",'role','full_name')}),
        ("Permissions", {"fields": ("is_staff", "is_active", 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2"),
        }),
    )

    search_fields = ("phone",)


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ('user', 'title', 'address','location','is_default')
    search_fields = ('title', 'address')


from django.contrib import admin
from users.models.addresses import Location
# Suppose location is the name of app :)
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ( 'location_point', )