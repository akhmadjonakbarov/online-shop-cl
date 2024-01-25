from shop_app.models import OrderItem
from rest_framework import serializers
from .product_serializer import ProductSerializer
from user_app.serializers import SellerSerializer, UserSerializerWithName


class OrderItemSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    user = UserSerializerWithName(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'seller', 'user', 'product', 'quantity', 'total_sum']
