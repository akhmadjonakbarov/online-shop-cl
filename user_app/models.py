from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin, Group
)
from django.db import models

from location_app.models import Region, District


class CustomUserManager(BaseUserManager):
    def create_user(self, phonenumber, password=None, **extra_fields):
        if not phonenumber:
            raise ValueError('The Email field must be set')
        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phonenumber, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phonenumber = models.CharField(unique=True, max_length=9)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['first_name', ]

    def __str__(self):
        return self.phonenumber


class UserLocation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.user.phonenumber} is from {self.region.name}')


class SuperAdminGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(CustomUser, related_name='superadmin_group')

    def __str__(self):
        return str(self.name)


class AdminGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(CustomUser, related_name='admin_group')

    def __str__(self):
        return str(self.name)
