from rest_framework import permissions

class IsReadOnlyOrUnauthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return not request.user or request.user.is_authenticated
    
    