from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, BooleanField, DateTimeField
from django.utils import timezone

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
