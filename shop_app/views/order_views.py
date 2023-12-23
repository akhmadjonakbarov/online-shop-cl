from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from shop_app.serializers.order_serializer import (OrderSerializer, OrderItemSerializer, Order, OrderItem)
from rest_framework import status

from user_app.models import CustomUser


class ListOrdersView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user: CustomUser = request.user
        orders = user.order_set.all()
        serializer = self.serializer_class(orders, many=True)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class DetailOrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        user: CustomUser = request.user
        order = user.order_set.get(id=id)
        serializer = self.serializer_class(order, many=False)
        return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)


class AddOrderView(GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            # Calculate total_price based on product prices or any logic you need
            total_price = sum(product['price'] for product in serializer.validated_data['products'])
            serializer.validated_data['total_price'] = total_price

            order = serializer.save()
            serializer = self.serializer_class(order, many=False)
            return Response({'success': 'true', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': 'false', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order
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
    serializer_class = OrderSerializer
    queryset = Order
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        user: CustomUser = request.user
        order = user.order_set.get(id=id)
        message = "Order was not deleted"
        if order is not None:
            order.delete()
            message = 'Order was deleted'
            return Response({'success': 'true', 'data': message}, status=status.HTTP_200_OK)
        return Response({'success': 'true', 'data': message}, status=status.HTTP_400_BAD_REQUEST)
