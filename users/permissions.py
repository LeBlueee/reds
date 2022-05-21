from rest_framework import permissions



class UpdateOwnUser(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        
        print(obj.id)
        print(request.user.id)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return obj.id == request.user.id



class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
