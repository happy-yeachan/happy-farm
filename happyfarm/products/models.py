from django.db import models
from users.models import CustomUser  # 유저 모델 import

class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')  # 작성자
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
