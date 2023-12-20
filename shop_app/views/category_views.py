from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)
from shop_app.serializers.category_serializer import (
    CategorySerializer, Category,
)
from rest_framework import status


class ListCategoriesView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category

    def get(self, request, format=None):
        categories = self.queryset.objects.all()
        serializer = self.serializer_class(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        serializer = self.serializer_class(product, many=False)
        return Response(serializer.data)


class UpdateCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        category = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        category = self.queryset.objects.get(id=id)
        message = "Product was not deleted"
        if category is not None:
            category.delete()
            message = "Product was deleted"
        return Response({'success': 'true', 'message': message, }, status=status.HTTP_200_OK)
