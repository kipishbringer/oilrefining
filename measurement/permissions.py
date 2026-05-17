from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return view.get_object().author == request.user or request.user.is_staff
