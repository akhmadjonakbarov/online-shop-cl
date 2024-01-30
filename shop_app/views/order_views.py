from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from shop_app.models import Product
from shop_app.serializers.order_serializer import (OrderItemSerializer, OrderItem, OrderItemLocation)
from rest_framework import status

from user_app.models import CustomUser


class ListOrdersView(GenericAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user: CustomUser = request.user
        if user.is_seller:
            orders = user.set_seller_orders.all()
            serializer = self.serializer_class(orders, many=True)
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            orders = user.set_user_orders.all()
            serializer = self.serializer_class(orders, many=True)
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class DetailOrderView(GenericAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        user: CustomUser = request.user
        if user.is_seller:
            order = user.set_seller_orders.get(id=id)
        else:
            order = user.set_user_orders.get(id=id)
        serializer = self.serializer_class(order, many=False)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class AddOrderView(GenericAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user: CustomUser = request.user
        seller = CustomUser.objects.get(id=request.data['sellerId'], is_seller=True)
        product = Product.objects.get(id=request.data['productId'])
        total_sum = product.price * int(request.data['quantity'])

        order_item = OrderItem.objects.create(
            product_id=request.data['productId'], quantity=request.data['quantity'],
            total_sum=total_sum, user=user, seller=seller
        )
        order_item.save()

        order_item_location = OrderItemLocation.objects.create(
            order_item=order_item, region_id=request.data['regionId'],
            district_id=request.data['districtId']
        )
        order_item_location.save()

        serializer = self.serializer_class(order_item, many=False)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class UpdateOrderView(GenericAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem
    permission_classes = [IsAuthenticated, ]

    def patch(self, request, id):
        order = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'false', 'data': serializer.errors}, status=status.HTTP_200_OK)


class DeleteOrderView(GenericAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        user: CustomUser = request.user
        order = user.set_user_orders.get(id=id)
        message = "Order was not deleted"
        if order is not None:
            order.delete()
            message = 'Order was deleted'
            return Response({'success': 'true', 'data': message}, status=status.HTTP_200_OK)
        return Response({'success': 'true', 'data': message}, status=status.HTTP_400_BAD_REQUEST)
