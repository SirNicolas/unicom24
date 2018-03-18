from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class PartnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.is_superuser:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.is_superuser:
                return True

        raise PermissionDenied


class CreditOrganizationPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.profile.is_credit_organization \
                or request.user.is_superuser:
            return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):

        if request.user.profile.is_credit_organization \
                or request.user.is_superuser:
            return True

        raise PermissionDenied
