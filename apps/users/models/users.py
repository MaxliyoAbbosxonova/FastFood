import re

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, BooleanField, DateTimeField
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from users.models.managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    class Role(TextChoices):
        ADMIN = "ADMIN", "admin"
        WAITER = "WAITER", "waiter"
        USER = "USER", "user"

    phone = CharField(max_length=13, unique=True)
    full_name = CharField(max_length=100)
    role = CharField(max_length=11, choices=Role.choices, default=Role.USER)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    def check_phone(self):
        digits = re.findall(r'\d', self.phone)
        if len(digits) > 9:
            raise ValidationError('Phone number must be at least 9 digits')
        phone = ''.join(digits)
        self.phone = phone.removeprefix('998')

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        self.check_phone()
        super().save(force_insert=force_insert, force_update=force_update, using=using)
