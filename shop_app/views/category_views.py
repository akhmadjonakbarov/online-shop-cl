from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

from shop_app.models import SellerCategory
from shop_app.serializers.category_serializer import (
    CategorySerializer, Category, SellerCategorySerializer,
)
from rest_framework import status
from user_app.models import CustomUser


class ListCategoriesView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = self.queryset.objects.all()
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
        # Get the category instance
        category = Category.objects.get(id=id)

        # Delete the category
        category.delete()

        # Respond with a success message
        return Response({"success": "true", "message": "Category deleted successfully"},
                        status=status.HTTP_200_OK)


class AddSellerCategoryView(GenericAPIView):
    serializer_class = SellerCategorySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user: CustomUser = request.user
        categoryId = request.data['categoryId']
        category = Category.objects.get(id=categoryId)
        sellerCategory = SellerCategory.objects.create(seller=user, category=category, is_active=True)
        sellerCategory.save()
        serializer = self.serializer_class(sellerCategory, many=False)
        return Response({'success': 'true', 'data': serializer.data, }, status=status.HTTP_200_OK)


class ListSellerCategoryView(GenericAPIView):
    serializer_class = SellerCategorySerializer

    def get(self, request):
        if request.user.is_authenticated:
            print("success")
            seller: CustomUser = request.user
            sellerCategories = SellerCategory.objects.filter(seller=seller, is_active=True)
            serializer = self.serializer_class(sellerCategories, many=True)
            return Response({'success': 'true', 'data': serializer.data, }, status=status.HTTP_200_OK)
        else:
            print("user not found")
            sellerCategories = SellerCategory.objects.filter(is_active=True)
            serializer = self.serializer_class(sellerCategories, many=True)
            return Response({'success': 'true', 'data': serializer.data, }, status=status.HTTP_200_OK)


class DeleteSellerCategoryView(GenericAPIView):
    serializer_class = SellerCategorySerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, seller_category_id):
        try:
            seller_category = SellerCategory.objects.get(id=seller_category_id)
            seller_category.delete()
            return Response({'success': 'true', 'data': 'Category was deleted', }, status=status.HTTP_200_OK)
        except SellerCategory.DoesNotExist:
            return Response({'success': 'false', 'message': 'Category does not exist', },
                            status=status.HTTP_400_BAD_REQUEST)
