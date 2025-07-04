# products/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSellerOrReadOnly(BasePermission):
    """
    판매자는 모든 권한, 그 외 유저는 조회만 가능
    """

    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS 는 모두 허용
        if request.method in SAFE_METHODS:
            return True
        # 그 외 요청은 로그인 + 판매자인 경우만 허용
        return request.user.is_authenticated and request.user.is_seller
    