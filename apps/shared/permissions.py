from django.contrib.auth.models import PermissionsMixin
from rest_framework.permissions import BasePermission


class IsWaiter(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Waiter' and request.user.is_authenticated:
            return True
        return False


class IsAdminOrWaiter(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PATCH']:
            return request.user.role == 'WAITER' or request.user.role == 'ADMIN' or request.user.is_superuser is True
        return False
