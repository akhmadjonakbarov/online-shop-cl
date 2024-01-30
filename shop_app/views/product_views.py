from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from shop_app.serializers.product_serializer import (ProductSerializer, Product)
from rest_framework import status
from shop_app.models import Category, SellerCategory


class ListProductsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product

    def get(self, request):
        products = self.queryset.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class DetailProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product

    def get(self, request, id):
        product = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(product, many=False)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class AddProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Product

    def post(self, request):
        try:
            user = request.user
            seller_category = SellerCategory.objects.get(id=request.data['sellerCategoryId'])
            product = Product.objects.create(
                user=user, category=seller_category, name=request.data['name'],
                description=request.data['description'],
                price=request.data['price'], coverImage=request.data['coverImage']
            )
            product.save()
            serializer = self.serializer_class(product, many=False)
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    permission_classes = (IsAuthenticated,)

    def patch(self, request, id):
        product = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'false', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        product = self.queryset.objects.get(id=id)
        message = "Product was not deleted"
        # Delete the category
        if product is not None:
            product.delete()
            message = "Product was deleted"
            return Response({'success': 'true', 'message': message}, status=status.HTTP_200_OK)
        return Response({'success': 'true', 'message': message}, status=status.HTTP_200_OK)
