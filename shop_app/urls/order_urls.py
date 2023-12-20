from django.urls import path
from shop_app.views.order_views import (
    ListOrdersView, DetailOrderView, AddOrderView, DeleteOrderView, UpdateOrderView
)

urlpatterns = [
    path('', view=ListOrdersView.as_view(),
         name='get_orders'),
    path('<int:id>/detail/',
         view=DetailOrderView.as_view(), name='detail_order'),
    path('add/',
         view=AddOrderView.as_view(), name='add_order'),
    path('<int:id>/update/',
         view=UpdateOrderView.as_view(), name='update_order'),
    path('<int:id>/delete/',
         view=DeleteOrderView.as_view(), name='delete_order'),
]
