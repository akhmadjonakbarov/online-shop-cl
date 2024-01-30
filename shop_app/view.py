from rest_framework.response import Response
from banner_app.serializers import Banner, BannerSerializer
from shop_app.serializers.category_serializer import Category, CategorySerializer, ProductSerializer, \
    SellerCategorySerializer, SellerCategory

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class HomeView(APIView):

    def get(self, request):
        products = []
        sellers_categories = SellerCategory.objects.all()
        seller_category_serializer = SellerCategorySerializer(sellers_categories, many=True)
        banners = Banner.objects.all()
        banner_serializer = BannerSerializer(banners, many=True)
        for seller_category in sellers_categories:
            products.append(seller_category.product_set.first())
        product_serializer = ProductSerializer(products, many=True)

        return Response(
            {
                'success': 'true',
                'data': {
                    'products': product_serializer.data,
                    'categories': seller_category_serializer.data,
                    'banners': banner_serializer.data
                }
            },
            status=status.HTTP_200_OK
        )
