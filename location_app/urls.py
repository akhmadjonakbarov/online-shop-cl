from django.urls import path
from .views import (
    ListRegionView, DetailRegionView
)

urlpatterns = [
    path('', view=ListRegionView.as_view(), name='get_regions'),
    path('<int:id>/detail/', view=DetailRegionView.as_view(), name='detail_region'),
]
