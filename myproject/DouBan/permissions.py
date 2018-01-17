from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义允许只允许一个对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        #对任何请求都允许读权限
        #因此，我们总是允许GET、HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:#SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True

        # 写权限只允许代码片段的所有者
        print(request.user)
        return obj.comment_user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    自定义允许只允许系统管理员编辑它。
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.is_superuser and
            request.user.is_authenticated
        )