from rest_framework.permissions import BasePermission


class IsOwnerOrAnonymousUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or not obj.user


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
