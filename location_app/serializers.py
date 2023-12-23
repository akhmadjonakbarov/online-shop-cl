from rest_framework import serializers
from .models import Region, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

    # def get_district(self, region: Region):
    #     districts = region.district_set.all()
    #     serializer = DistrictSerializer(districts, many=True)
    #     return serializer.data
