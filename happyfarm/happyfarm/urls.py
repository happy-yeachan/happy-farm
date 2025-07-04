from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserViewSet, SignUpView
from products.views import ProductViewSet
from orders.views import OrderViewSet
from carts.views import CartItemViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignUpView.as_view(), name='signup'),

]
