from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from apps.models import Order, Food, OrderItem, User, Category


# Register your models here.


@admin.register(Food)
class FoodAdmin(ModelAdmin):
    list_display =('image','name','price','category_id')
    search_fields =('name','id')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="90" height="90" style="object-fit: cover;" />'
            )
        return "—"

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display =('user','name','total_price','delivery_address','created_at')
    search_fields =('name','id')

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display =('order','food','quantity','price')

@admin.register(User)
class OrderAdmin(UserAdmin):
    list_display = ('id', "phone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    ordering = ("phone",)

    fieldsets = (
        (None, {"fields": ( "phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active",'groups','user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ( "phone", "password1", "password2"),
        }),
    )

    search_fields = ( "phone",)

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display =('id','name')
    search_fields =('id','name')
