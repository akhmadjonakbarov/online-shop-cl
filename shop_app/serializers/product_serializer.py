from shop_app.models import (
    Category, Product,
    ProductImage, Review
)
from rest_framework import serializers


class _CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = _CategorySerializer()

    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name',
            'description', 'price', 'rating',
            'coverImage', 'images',
        )

    def get_images(self, product: Product):
        images = product.set_images.all()
        serializer = ProductSerializer(images, many=True)
        return serializer.data
