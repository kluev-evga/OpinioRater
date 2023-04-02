from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.is_staff)
        )  # TODO: Сделать логику superusera
