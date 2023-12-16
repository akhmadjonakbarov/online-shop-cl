from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from shop_app.models import CustomUser
from .serializers import LocationSerializer, Location


class ListLocationView(GenericAPIView):
    serializer_class = LocationSerializer
    queryset = Location

    def get(self, request):
        locations = self.queryset.objects.all()
        serializer = self.serializer_class(locations, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class AddLocationView(GenericAPIView):
    serializer_class = LocationSerializer
    queryset = Location
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        location = None
        user: CustomUser = request.user
        if user.superadmin_group.exists():
            location = self.queryset.objects.create(name=request.data['name'], user=user)
            location.save()
            serializer = self.serializer_class(location, many=False)
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'detail': 'You are not superadmin'})
