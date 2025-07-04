# products/serializers.py

from rest_framework import serializers
from .models import Product
from utils.imgbb import imgbb# S3 업로드 함수 임포트

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_url', 'image']  # image는 업로드용, image_url은 DB 저장

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        instance = super().create(validated_data)

        if image:
            image_url = imgbb(image)  # S3 업로드 함수 호출
            instance.image_url = image_url
            instance.save()

        return instance
