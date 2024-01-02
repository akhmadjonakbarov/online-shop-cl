from django.contrib import admin
from .models import (
    Category, Product,
    ProductImage, Review,
    Order, OrderItem, SellerCategory
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SellerCategory)

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     pass
#
# class BookInline(admin.TabularInline):
#     model = Book
#
#
# class ClotheInline(admin.TabularInline):
#     model = Clothe
#
#
# class ProductClotheAdmin(admin.ModelAdmin):
#
#     inlines = (ClotheInline,)
#
#
# class ProductBookAdmin(admin.ModelAdmin):
#     inlines = (BookInline,)
