from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request == 'POST':
            return bool(request.user and request.user.is_staff)
        return True
