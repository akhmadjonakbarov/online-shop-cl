from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token

from user_app.models import CustomUser
from shop_app.serializers.order_serializer import OrderSerializer


class LoginSerializer(serializers.Serializer):
    phonenumber = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializerWithToken(serializers.ModelSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isSeller = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name', 'isSeller', 'isAdmin', 'access', 'refresh')

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

    def get_isAdmin(self, user: CustomUser):
        return user.is_staff


class SellerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name')

    def get_name(self, user: CustomUser):
        name = user.first_name
        if name == '':
            name = user.phonenumber
        return name
