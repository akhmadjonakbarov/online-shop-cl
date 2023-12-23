from rest_framework.response import Response
from banner_app.serializers import Banner, BannerSerializer
from shop_app.serializers.category_serializer import Category, CategorySerializer, ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status


# Create your views here.
class HomeView(GenericAPIView):

    def get(self, request):
        products = []
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        banners = Banner.objects.all()
        banner_serializer = BannerSerializer(banners, many=True)
        for category in categories:
            products.append(category.product_set.first())
        product_serializer = ProductSerializer(products, many=True)

        return Response(
            {
                'success': 'true',
                'data': {
                    'products': product_serializer.data,
                    'categories': category_serializer.data,
                    'banners': banner_serializer.data
                }
            },
            status=status.HTTP_200_OK
        )
