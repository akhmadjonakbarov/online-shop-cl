from django.db import models


# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to='banner-images/')

    def __str__(self):
        return str(self.image)
