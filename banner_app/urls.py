from django.urls import path
from .views import (
    ListBannerView, BannerAddView, BannerDeleteView
)

urlpatterns = [
    path('', view=ListBannerView.as_view(), name='banners-get'),
    path('banners/add/', BannerAddView.as_view(), name='banner-add'),
    path('banners/<int:id>/delete/', BannerDeleteView.as_view(), name='banner-delete'),

]
