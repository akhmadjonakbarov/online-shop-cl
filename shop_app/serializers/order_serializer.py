from shop_app.models import OrderItem, OrderItemLocation
from rest_framework import serializers
from .product_serializer import ProductSerializer
from user_app.serializers import SellerSerializer, UserSerializerWithName
from location_app.serializers import RegionSerializer, DistrictSerializer


class OrderItemLocationSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = OrderItemLocation
        fields = ("region", "district")


class OrderItemSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    user = UserSerializerWithName(read_only=True)
    product = ProductSerializer(read_only=True)
    location = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'seller', 'user', 'product', 'quantity', 'total_sum', 'location', 'createdAt']

    def get_location(self, order_item: OrderItem):
        locations = order_item.orderitemlocation_set.all()
        if locations:
            serializer = OrderItemLocationSerializer(locations, many=True)
            return serializer.data
        return None
