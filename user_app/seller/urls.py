from django.urls import path
from user_app.seller.views import (
    ListSellerView
)

urlpatterns = [
    path('', ListSellerView.as_view(), name='get_seller'),
]
