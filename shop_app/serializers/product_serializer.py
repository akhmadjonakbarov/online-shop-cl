from shop_app.models import (
    Product,
    Review, SellerCategory
)
from rest_framework import serializers
from user_app.serializers import UserSerializerWithName


class _SellerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerCategory
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializerWithName(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'seller_category', 'name',
            'description', 'price', 'rating',
            'coverImage', 'user'
        )
