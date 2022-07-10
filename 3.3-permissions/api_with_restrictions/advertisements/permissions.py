from rest_framework import permissions
from rest_framework.permissions import BasePermission

from .models import Advertisement


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.creator or bool(request.user and request.user.is_staff)



