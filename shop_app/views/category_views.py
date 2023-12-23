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
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = self.queryset.objects.filter(isDeleted=False)
        serializer = self.serializer_class(categories, many=True)
        return Response({'success': 'true', 'data': serializer.data, }, status=status.HTTP_200_OK)


class AddCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        serializer = self.serializer_class(category, many=False)
        return Response(serializer.data)


class DetailCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Category

    def get(self, request, id):
        category = self.queryset.objects.get(id=id, is_delete=False)
        serializer = self.serializer_class(category, many=False)
        return Response({'success': 'true', 'data': serializer.data, }, status=status.HTTP_200_OK)


class UpdateCategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        category = self.queryset.objects.get(id=id)
        message = "Product was not deleted"
        if category is not None:
            category.isDeleted = True
            category.save()
        return Response({'success': 'true', 'message': message, }, status=status.HTTP_200_OK)


class AddSellerCategory(GenericAPIView):

    def post(self, request):
        pass
