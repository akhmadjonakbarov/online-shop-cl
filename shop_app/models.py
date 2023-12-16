from django.db import models
from user_app.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=250)
    about = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='category-image/')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="set_products_user")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="set_products_category")
    name = models.CharField(max_length=250)
    description = models.TextField()
    coverImage = models.ImageField(upload_to=f"productImages/")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="set_images")
    image = models.ImageField(upload_to=f"productImages/{product.name}")

    def __str__(self) -> str:
        return f"Picture of {self.product.name}"


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='set_reviews_user')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='set_reviews_product')
    comment = models.TextField()

    def __str__(self) -> str:
        return str(f"{self.user}'s comment")


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(f'{self.user.email}\'s order')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order)

