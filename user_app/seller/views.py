from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from user_app.models import CustomUser
from user_app.serializers import UserSerializerWithToken


class ListSellerView(GenericAPIView):
    serializer_class = UserSerializerWithToken
    queryset = CustomUser

    def get(self, request):
        sellers = self.queryset.objects.filter(is_seller=True)
        serializer = self.serializer_class(sellers, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
