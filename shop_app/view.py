from rest_framework.response import Response
from banner_app.serializers import Banner, BannerSerializer
from shop_app.serializers.category_serializer import Category, CategorySerializer, ProductSerializer, \
    SellerCategorySerializer, SellerCategory
from shop_app.models import Product

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class HomeView(APIView):

    def get(self, request):
        products = Product.objects.all()
        sellers_categories = SellerCategory.objects.all()
        banners = Banner.objects.all()
        seller_category_serializer = SellerCategorySerializer(sellers_categories, many=True)
        banner_serializer = BannerSerializer(banners, many=True)
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
