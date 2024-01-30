from shop_app.models import (
    Product,
    Review, SellerCategory
)
from rest_framework import serializers


class _SellerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerCategory
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # seller_category = _SellerCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'seller_category', 'name',
            'description', 'price', 'rating',
            'coverImage'
        )
