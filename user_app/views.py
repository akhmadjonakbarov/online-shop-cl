from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_app.serializers import (UserSerializerWithToken, LoginSerializer)
from .models import CustomUser, UserLocation, Location


class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializerWithToken

    def post(self, request):
        data = request.data
        try:
            user = CustomUser.objects.create(
                first_name=data['first_name'],
                phonenumber=data['phonenumber'],
                is_seller=data['isSeller'],
                password=make_password(str(data['password'])),
            )
            user.save()
            location = Location.objects.create(name=data['location'])
            location.save()
            userLocation = UserLocation.objects.create(user=user, location=location)
            userLocation.save()
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            message = {'detail': 'User with this phonenumber aready exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(GenericAPIView):
    serializer_class = UserSerializerWithToken
    queryset = CustomUser

    def post(self, request):
        try:
            user = CustomUser.objects.get(phonenumber=request.data['phonenumber'])
            if user.is_delete is not True:
                serializer = LoginSerializer(data=request.data)
                if serializer.is_valid():
                    phonenumber = serializer.validated_data['phonenumber']
                    password = serializer.validated_data['password']
                    user = authenticate(request, phonenumber=phonenumber, password=password)
                    if user is not None:
                        serializer = self.serializer_class(user, many=False)
                        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'data': 'User was deleted'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'data': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)


class GetUserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerWithToken

    def get(self, request):
        user: CustomUser = request.user
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
