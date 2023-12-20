from django.urls import path
from shop_app.views.product_views import (
    ListProductsView, DetailProductView, AddProductView,
    UpdateProductView, DeleteProductView
)

urlpatterns = [
    path('', view=ListProductsView.as_view(), name='get_products'),
    path('<int:id>/detail/', view=DetailProductView.as_view(), name='detail_product'),
    path('add/', view=AddProductView.as_view(), name='add_product'),
    path('<int:id>/update/', view=UpdateProductView.as_view(), name='update_product'),
    path('<int:id>/delete/', view=DeleteProductView.as_view(), name='delete_product'),
]
