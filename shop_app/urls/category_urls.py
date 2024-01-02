from django.urls import path
from shop_app.views.category_views import (
    ListCategoriesView, AddCategoryView, UpdateCategoryView, DeleteCategoryView, ListSellerCategoryView,
    AddSellerCategoryView
)

urlpatterns = [
    path('', view=ListCategoriesView.as_view(), name='get_categories'),
    path('add/', view=AddCategoryView.as_view(), name='add_category'),
    path('<int:id>/update/', view=UpdateCategoryView.as_view(), name='update_category'),
    path('<int:id>/delete/', view=DeleteCategoryView.as_view(), name='delete_category'),
    path('seller-category/add/', view=AddSellerCategoryView.as_view(), name='add_seller_category'),
    path('seller-categories/', view=ListSellerCategoryView.as_view(), name='list_seller_category'),
]
