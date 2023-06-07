from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self,request,view):
        """If the user who checks the url is not the admin, he can 
        only get the data. Only admin users can access and write to it

        Args:
            request (_type_): _description_
            view (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return  bool(request.user and request.user.is_staff)

class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view, obj):
        """If the user who checks for the movie review is not the user
        who reviwed the movie, they can only be given get access
        If the user who is checking the url is the reviewer, he can be given write access
        Args:
            request (_type_): _description_
            view (_type_): _description_
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff