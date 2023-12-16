from django.urls import path
from shop_app.views.category_views import (
    GetCategoriesView, AddCategoryView,
)
urlpatterns = [
    path('', view=GetCategoriesView.as_view(),
         name='get_categories'),
    # path('categories/<int:id>/detail',
    #      view=GetCategoryView.as_view(), name='detail_category'),
    # path('categories/add/',
    #      view=AddCategoryView.as_view(), name='add_category'),
    # path('categories/<int:id>/update',
    #      view=UpdateCategoryView.as_view(), name='update_category'),
    # path('categories/<int:id>/delete',
    #      view=DeleteCategoryView.as_view(), name='delete_category'),
]
