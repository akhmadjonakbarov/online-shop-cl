from django.db import models


# Create your models here.
class Banner(models.Model):
    image = models.CharField(max_length=3000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)
