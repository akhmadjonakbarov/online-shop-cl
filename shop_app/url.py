from django.urls import path
from .view import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home_list')
]
