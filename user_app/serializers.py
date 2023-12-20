from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from location_app.serializers import LocationSerializer
from user_app.models import CustomUser


class UserSerializerWithToken(serializers.ModelSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isSuperAdmin = serializers.SerializerMethodField(read_only=True)
    locations = serializers.SerializerMethodField(read_only=True)
    isSeller = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phonenumber', 'name', 'isAdmin', 'isSuperAdmin', 'access', 'refresh', 'locations', 'isSeller')

    def get_access(self, user: CustomUser):
        token: Token = RefreshToken.for_user(user)
        return str(token.access_token)

    def get_refresh(self, user: CustomUser):
        token: Token = RefreshToken.for_user(user)
        return str(token)

    def get_isAdmin(self, user: CustomUser):
        return user.is_staff

    def get_isSeller(self, user: CustomUser):
        return user.is_seller

    def get_name(self, user: CustomUser):
        name = user.first_name
        if name == '':
            name = user.email
        return name

    def get_locations(self, user: CustomUser):
        locations = user.userlocation_set.all()
        serializer = LocationSerializer(locations, many=True)
        return serializer.data

    def get_isSuperAdmin(self, user: CustomUser):
        if user.superadmin_group.exists():
            return True
        else:
            return False


class UserRegisterSerializerWithToken(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'phonenumber', 'password')
