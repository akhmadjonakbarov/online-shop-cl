from django.urls import path
from user_app.seller.views import (
    ListSellerView, DeleteSellerView
)

urlpatterns = [
    path('', ListSellerView.as_view(), name='get_seller'),
    path('<int:id>/delete/', DeleteSellerView.as_view(), name='delete_seller'),
]
