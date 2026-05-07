from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, DecimalField, TextField, BooleanField, DateTimeField



class Address(Model):
    user = ForeignKey('User', on_delete=CASCADE, related_name='addresses')
    title = CharField(max_length=100)
    address = CharField(max_length=100)
    longitude = DecimalField(max_digits=9, decimal_places=7)
    latitude = DecimalField(max_digits=9, decimal_places=7)
    entrance = CharField(max_length=20, null=True, blank=True)
    floor = CharField(max_length=20, null=True, blank=True)
    apartment = CharField(max_length=20, null=True, blank=True)
    comment = TextField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_default = BooleanField(default=False)

    def __str__(self):
        return self.title
