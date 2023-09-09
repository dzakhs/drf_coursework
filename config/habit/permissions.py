from rest_framework.permissions import BasePermission
from config.users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False




class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцом'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.useer:
            return True
        return False