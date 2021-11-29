from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class ReadOnly(BasePermission):
    def has_permission(self, request: Request, view):
        return request.method in SAFE_METHODS
