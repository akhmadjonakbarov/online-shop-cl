from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return str(self.name)
