from django.urls import path
from shop_app.views.category_views import (
    ListCategoriesView, AddCategoryView, UpdateCategoryView, DeleteCategoryView
)

urlpatterns = [
    path('', view=ListCategoriesView.as_view(), name='get_categories'),
    path('add/', view=AddCategoryView.as_view(), name='add_category'),
    path('<int:id>/update/', view=UpdateCategoryView.as_view(), name='update_category'),
    path('<int:id>/delete/', view=DeleteCategoryView.as_view(), name='delete_category'),
]
