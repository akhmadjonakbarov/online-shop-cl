from rest_framework import serializers
from shop_app.models import Category, SellerCategory
from user_app.serializers import SellerSerializer
from shop_app.serializers.product_serializer import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class SellerCategorySerializer(serializers.ModelSerializer):
    seller = SellerSerializer(many=False)
    category = CategorySerializer(many=False)
    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SellerCategory
        fields = ('id', 'seller', 'category', 'is_active', 'products')

    def get_products(self, seller_category: SellerCategory):
        products = seller_category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data
