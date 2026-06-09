from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import TextField, EmailField, CharField, SlugField, TimeField, IntegerField, \
    PositiveIntegerField, BooleanField, DateTimeField
from django_tenants.models import TenantMixin, DomainMixin
from location_field.models.spatial import LocationField

from users.models import Address
from users.models.addresses import Location


# Create your models here.

class RestaurantsCategory(Model):
    name=CharField(max_length=100)
    icon=ImageField(null=True,blank=True,upload_to='media/res_categories/')



class Restaurants(TenantMixin):
    name=CharField(max_length=100)
    slug=SlugField(unique=True,null=True,blank=True)
    description=TextField(blank=True,null=True)
    logo=ImageField(blank=True,null=True,upload_to='media/logo/')
    phone=CharField(max_length=20,default='901234567')
    email=EmailField(blank=True,null=True)
    location_point=LocationField(default=Point(51.67, 32.65))
    opening_time=TimeField(auto_now_add=True)
    closing_time=TimeField(auto_now_add=True)
    min_order_amount=IntegerField(default=1)
    delivery_fee=PositiveIntegerField(default=3000)
    is_open = BooleanField(default=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Domain(DomainMixin):
    pass