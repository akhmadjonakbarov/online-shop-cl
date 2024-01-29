from shop_app.models import (
    Category, Product,
    Review, SellerCategory
)
from rest_framework import serializers


class _SellerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerCategory
        fields = ('id', 'seller', 'category')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = _SellerCategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name',
            'description', 'price', 'rating',
            'coverImage'
        )
