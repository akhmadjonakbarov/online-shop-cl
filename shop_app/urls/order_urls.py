from django.urls import path
from shop_app.views.order_views import (
    ListOrdersView, DetailOrderView, AddOrderView, DeleteOrderView, UpdateOrderView
)

urlpatterns = [
    path('', view=ListOrdersView.as_view(),
         name='get_orders'),
    path('orders/<int:id>/detail/',
         view=DetailOrderView.as_view(), name='detail_order'),
    path('orders/add/',
         view=AddOrderView.as_view(), name='add_order'),
    path('orders/<int:id>/update/',
         view=UpdateOrderView.as_view(), name='update_order'),
    path('orders/<int:id>/delete/',
         view=DeleteOrderView.as_view(), name='delete_order'),
]
