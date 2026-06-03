from django.contrib.gis.geos import Point
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, TextField, BooleanField, DateTimeField
from location_field.models.spatial import LocationField


class Location(Model):
    location_point = LocationField(based_fields=['city'], zoom=7, default=Point(51.67, 32.65), null=True, blank=True)


class Address(Model):
    user = ForeignKey('User', on_delete=CASCADE, related_name='addresses')
    title = CharField(max_length=100)
    address = CharField(max_length=100)
    location = ForeignKey('Location', on_delete=CASCADE, related_name='addresses', null=True, blank=True)
    entrance = CharField(max_length=20, null=True, blank=True)
    floor = CharField(max_length=20, null=True, blank=True)
    apartment = CharField(max_length=20, null=True, blank=True)
    comment = TextField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_default = BooleanField(default=False)

    def __str__(self):
        return self.title
