from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from shop_app.serializers.order_serializer import (OrderSerializer, OrderItemSerializer, Order, OrderItem)
from rest_framework import status

from user_app.models import CustomUser


class ListOrdersView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order

    def get(self, request, format=None):
        user: CustomUser = request.user
        orders = user.order_set.all()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailOrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order

    def get(self, request, id):
        user: CustomUser = request.user
        order = user.order_set.get(id=id)
        serializer = self.serializer_class(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddOrderView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            # Calculate total_price based on product prices or any logic you need
            total_price = sum(product['price'] for product in serializer.validated_data['products'])
            serializer.validated_data['total_price'] = total_price

            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        order = self.queryset.objects.get(id=id)
        serializer = self.serializer_class(
            instance=order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            message = "Product was deleted"
        return Response({'message': message}, status=status.HTTP_200_OK)
