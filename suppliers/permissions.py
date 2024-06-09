from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    '''Является ли user создателем obj'''

    def has_object_permission(self, request, view, obj):
        res = True if request.user == obj.user else False
        return res


class IsActive(BasePermission):
    '''Является ли user активным пользователем'''

    def has_object_permission(self, request, view, obj):
        res = True if request.user.is_active else False
        return res
