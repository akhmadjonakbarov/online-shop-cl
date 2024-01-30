from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token

from user_app.models import CustomUser
from user_app.models import UserLocation
from location_app.serializers import DistrictSerializer, RegionSerializer


class UserLocationSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = UserLocation
        fields = ['region', 'district']


class LoginSerializer(serializers.Serializer):
    phonenumber = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializerWithToken(serializers.ModelSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isSeller = serializers.SerializerMethodField(read_only=True)
    location = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name', 'isSeller', 'isAdmin', 'access', 'refresh', 'location')

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

    def get_location(self, user: CustomUser):
        user_location = UserLocation.objects.get(user=user)
        serializer = UserLocationSerializer(user_location, many=False)
        return serializer.data


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name')


class UserSerializerWithName(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name')

    def get_name(self, user: CustomUser):
        name = user.first_name
        if name == '':
            name = user.phonenumber
        return name


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
