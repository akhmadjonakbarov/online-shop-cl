from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import BannerSerializer, Banner


# Create your views here.
class ListBannerView(GenericAPIView):
    serializer_class = BannerSerializer
    queryset = Banner
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        banners = self.queryset.objects.all()
        serializer = self.serializer_class(banners, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class BannerAddView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BannerDeleteView(APIView):
    def delete(self, request, id):
        try:
            banner = Banner.objects.get(id=id)
        except Banner.DoesNotExist:
            return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)

        banner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
