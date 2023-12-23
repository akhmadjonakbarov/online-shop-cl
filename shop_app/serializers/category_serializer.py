from rest_framework import serializers
from shop_app.models import Category
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
