from rest_framework import permissions

class IsReadOnlyOrUnauthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return not request.user or request.user.is_authenticated
    

class AllowUnauthenticatedComment(permissions.BasePermission):
    """
    Custom permission to allow unauthenticated users to create comments.
    """

    def has_permission(self, request, view):
        # Allow unauthenticated users to create comments (POST)
         return request.method == 'POST' or request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow everyone to view comments
        return True

    
class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the author of the object
        return obj.author == request.user #and request.method in permissions.SAFE_METHODS

    def has_permission(self, request, view):
        # Allow creation of new posts for authenticated users
        return request.method == 'PUT' and request.user.is_authenticated
    
    def has_object_write_permission(self, request, view, obj):
        # Allow write (PUT, DELETE) only if the user is the author
        return obj.author == request.user
    
