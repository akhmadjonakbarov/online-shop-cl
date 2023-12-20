from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from user_app.serializers import (UserRegisterSerializerWithToken, UserSerializerWithToken)
from .models import CustomUser


class UserRegisterView(GenericAPIView):
    serializer_class = UserRegisterSerializerWithToken

    def post(self, request):
        data = request.data
        try:
            user = CustomUser.objects.create(
                first_name=data['first_name'],
                phonenumber=data['phonenumber'],
                password=make_password(str(data['password'])),

            )
            user.save()

            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:

            message = {'detail': 'User with this phonenumber aready exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(GenericAPIView):
    serializer_class = UserSerializerWithToken

    def post(self, request):
        user = CustomUser.objects.get(phonenumber=request.data['phonenumber'])
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)


class GetUserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerWithToken

    def get(self, request):
        user: CustomUser = request.user
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
