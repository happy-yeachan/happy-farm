# carts/models.py

from django.db import models
from users.models import CustomUser
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # 같은 상품을 중복으로 담지 않도록

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x{self.quantity}"
