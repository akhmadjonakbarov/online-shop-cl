from django.db import models


# Create your models here.
class Banner(models.Model):
    image = models.CharField(max_length=3000)

    def __str__(self):
        return str(self.image)
