from django.db import models


# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='banner-images/')

    def __str__(self):
        return str(self.title)
