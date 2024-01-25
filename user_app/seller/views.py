from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from user_app.models import CustomUser
from user_app.serializers import UserSerializerWithName


class ListSellerView(GenericAPIView):
    serializer_class = UserSerializerWithName
    queryset = CustomUser

    def get(self, request):
        sellers = self.queryset.objects.filter(is_seller=True, is_delete=False)
        serializer = self.serializer_class(sellers, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class UpdateSellerView(GenericAPIView):
    serializer_class = UserSerializerWithName
    queryset = CustomUser

    def patch(self, request, id):
        user = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'true', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeleteSellerView(GenericAPIView):
    queryset = CustomUser

    def delete(self, request, id):
        seller = self.queryset.objects.get(id=id)
        seller.is_delete = True
        seller.save()
        return Response({'success': 'true', 'message': 'Seller was deleted', }, status=status.HTTP_200_OK)
