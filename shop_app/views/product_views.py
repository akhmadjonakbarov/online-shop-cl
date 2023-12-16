from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from shop_app.serializers.product_serializer import (ProductSerializer, Product)
from rest_framework import status


class GetProductsView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product

    def get(self, request, format=None):
        products = self.queryset.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product

    def get(self, request, id):
        product = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        serializer = self.serializer_class(product, many=False)
        return Response(serializer.data)


class UpdateProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        product = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        product = self.queryset.objects.get(id=id)
        message = "Product was not deleted"
        if product is not None:
            product.delete()
            message = "Product was deleted"
        return Response({'message': message}, status=status.HTTP_200_OK)
