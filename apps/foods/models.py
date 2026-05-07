from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, DecimalField, TextField, BooleanField, DateTimeField


class Category(Model):
    name = CharField(max_length=100)
    description = TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Food(Model):
    name = CharField(max_length=100)
    description = TextField(max_length=500, null=True, blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    category_id = ForeignKey('Category', on_delete=CASCADE)
    is_available = BooleanField(default=True)
    image = ImageField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
