from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token

from location_app.serializers import LocationSerializer
from user_app.models import CustomUser
from shop_app.serializers.order_serializer import OrderSerializer


class LoginSerializer(serializers.Serializer):
    phonenumber = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializerWithToken(serializers.ModelSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    isSuperAdmin = serializers.SerializerMethodField(read_only=True)
    isSeller = serializers.SerializerMethodField(read_only=True)
    orders = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name', 'isSeller', 'isSuperAdmin', 'access', 'refresh', 'orders')

    def get_access(self, user: CustomUser):
        token: Token = RefreshToken.for_user(user)
        return str(token.access_token)

    def get_refresh(self, user: CustomUser):
        token: Token = RefreshToken.for_user(user)
        return str(token)

    def get_isSeller(self, user: CustomUser):
        return user.is_seller

    def get_name(self, user: CustomUser):
        name = user.first_name
        if name == '':
            name = user.phonenumber
        return name

    def get_orders(self, user: CustomUser):
        if user.is_seller is True:
            orders = user.set_seller_orders.all()
            serializer = OrderSerializer(orders, many=True)
            return serializer.data
        else:
            orders = user.set_user_orders.all()
            serializer = OrderSerializer(orders, many=True)
            return serializer.data

    def get_isSuperAdmin(self, user: CustomUser):
        if user.superadmin_group.exists():
            return True
        else:
            return False
