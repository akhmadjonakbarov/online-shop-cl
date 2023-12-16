from django.db import models
from user_app.models import CustomUser


# Create your models here.
class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)
