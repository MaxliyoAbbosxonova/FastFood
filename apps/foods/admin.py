from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from foods.models import Food, Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Food)
class FoodAdmin(ModelAdmin):
    list_display = ('image', 'name', 'price', 'category_id')
    search_fields = ('name', 'id')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="90" height="90" style="object-fit: cover;" />'
            )
        return "—"
