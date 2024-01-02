from rest_framework import serializers
from shop_app.models import Category, SellerCategory
from user_app.models import CustomUser
from user_app.serializers import SellerSerializer
from ..serializers.product_serializer import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'products')

    def get_products(self, category: Category):
        products = category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data


class _CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SellerCategorySerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SellerCategory
        fields = ('id', 'seller', 'category', 'is_active')

    def get_seller(self, user: CustomUser):
        user = CustomUser.objects.get(id=user.id, is_seller=True)
        serializer = SellerSerializer(user, many=False)
        return serializer.data

    def get_category(self, category: Category):
        category = Category.objects.get(category=category)
        serializer = _CategorySerializer(category, many=False)
        return serializer.data
