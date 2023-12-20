from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import BannerSerializer, Banner


# Create your views here.
class ListBannerView(GenericAPIView):
    serializer_class = BannerSerializer
    queryset = Banner

    def get(self, request):
        banners = self.queryset.objects.all()
        serializer = self.serializer_class(BannerSerializer)
        return
