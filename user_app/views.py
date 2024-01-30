from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_app.serializers import (UserSerializerWithToken, LoginSerializer, UpdateUserSerializer)
from .models import CustomUser, UserLocation


class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializerWithToken

    def post(self, request):
        data = request.data
        global isSeller
        isSeller = None
        try:
            if request.data['isSeller'] is not None:
                if request.data['isSeller'] == 'true':
                    isSeller = True
                else:
                    isSeller = False
            else:
                isSeller = False
            if isSeller:
                user = CustomUser.objects.create(
                    first_name=data['first_name'],
                    phonenumber=data['phonenumber'],
                    is_seller=isSeller,
                    password=make_password(str(data['password'])),
                )
                user.save()
                userLocation = UserLocation.objects.create(
                    user=user, region_id=request.data['regionId'],
                    district_id=request.data['districtId'],
                )
                userLocation.save()
                serializer = self.serializer_class(user, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                user = CustomUser.objects.create(
                    first_name=data['first_name'],
                    phonenumber=data['phonenumber'],
                    is_seller=isSeller,
                    password=make_password(str(data['password'])),
                )
                user.save()
                userLocation = UserLocation.objects.create(
                    user=user, region_id=request.data['regionId'],
                    district_id=request.data['districtId'],
                )
                userLocation.save()
                serializer = self.serializer_class(user, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            message = {'message': 'User with this phonenumber aready exists'}
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
                        return Response({'message': 'Invalid username or password'},
                                        status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'User was deleted'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(GenericAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        user: CustomUser = request.user

        # Ensure that 'phone_number' and 'name' are present in the request data
        phone_number = request.data.get('phone_number')
        name = request.data.get('first_name')

        # Update user fields individually if they are provided
        if phone_number is not None:
            user.phone_number = phone_number
        if name is not None:
            user.first_name = name

        # Save the user object
        user.save()

        # Remove 'name' from the request data before passing it to the serializer
        user_data = request.data.copy()
        user_data.pop('name', None)

        # Use the serializer to update the remaining fields
        serializer = UserSerializerWithToken(user, data=user_data, partial=True)
        if serializer.is_valid():
            serializer.save()

        # Serialize the updated user and return the response
        response_serializer = UserSerializerWithToken(user, many=False)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class UpdateUserLocation(GenericAPIView):
    serializer_class = UserSerializerWithToken
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        user: CustomUser = request.user
        user_location = UserLocation.objects.get(user=user)
        user_location.region_id = request.data['regionId']
        user_location.district_id = request.data['districtId']
        user_location.save()
        serializer = self.serializer_class(user, many=False)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class GetUserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerWithToken

    def get(self, request):
        user: CustomUser = request.user
        serializer = self.serializer_class(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
