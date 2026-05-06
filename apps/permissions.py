from rest_framework.permissions import BasePermission


class Is_Waiter(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Waiter' and request.user.is_authenticated :
            return True