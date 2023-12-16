from django.urls import path
from shop_app.views.product_views import (
    GetProductsView, DetailProductView, AddProductView,
    UpdateProductView, DeleteProductView
)

urlpatterns = [
    path('', view=GetProductsView.as_view(),
         name='get_products'),
    path('products/<int:id>/detail/',
         view=DetailProductView.as_view(), name='detail_product'),
    path('products/add/',
         view=AddProductView.as_view(), name='add_product'),
    path('products/<int:id>/update/',
         view=UpdateProductView.as_view(), name='update_product'),
    path('products/<int:id>/delete/',
         view=DeleteProductView.as_view(), name='delete_product'),
]
