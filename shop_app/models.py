from django.db import models

from location_app.models import District, Region
from user_app.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="set_products_user")
    seller_category = models.ForeignKey(
        'SellerCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField()
    coverImage = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='set_reviews_user')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='set_reviews_product')
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(f"{self.user}'s comment")


class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='set_user_orders')
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='set_seller_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class OrderItemLocation(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class SellerCategory(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.seller.first_name)
