from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import BannerSerializer, Banner


# Create your views here.
class ListBannerView(GenericAPIView):
    serializer_class = BannerSerializer
    queryset = Banner

    def get(self, request):
        banners = self.queryset.objects.all()
        serializer = self.serializer_class(banners, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
