from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import RegionSerializer, Region, DistrictSerializer, District


class ListRegionView(GenericAPIView):
    serializer_class = RegionSerializer
    queryset = Region

    def get(self, request):
        locations = self.queryset.objects.all()
        serializer = self.serializer_class(locations, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class DetailRegionView(GenericAPIView):
    serializer_class = DistrictSerializer
    queryset = District

    def get(self, request, id):
        districts = self.queryset.objects.filter(region_id=id)
        serializer = self.serializer_class(districts, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
