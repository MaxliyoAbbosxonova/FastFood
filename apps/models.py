from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, IntegerField, TextField, BooleanField, DateTimeField
from django.utils import timezone


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("User must have a phone number")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using='default')
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
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

    objects=UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name


class Category(Model):
    name = CharField(max_length=100)
    description = TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Food(Model):
    name = CharField(max_length=100)
    description = TextField(max_length=500, null=True, blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    category_id = ForeignKey(Category, on_delete=CASCADE)
    is_available = BooleanField(default=True)
    image = ImageField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(Model):
    class Status(TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on_the_way'
        DELIVERED = 'DELIVERED', 'delivered'

    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    status=CharField(choices=Status.choices, default=Status.PENDING, max_length=10)
    total_price = DecimalField(max_digits=10, decimal_places=2)
    delivery_address = TextField(max_length=500, null=True, blank=True)
    latitude = DecimalField(max_digits=9, decimal_places=7)
    longitude = DecimalField(max_digits=9, decimal_places=7)
    estimated_time = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    food = ForeignKey(Food, on_delete=CASCADE)
    quantity = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
