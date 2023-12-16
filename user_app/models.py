from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin, Group
)
from django.db import models

from location_app.models import Location


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class UserLocation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.user.email} is from {self.location.name}')


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
