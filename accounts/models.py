from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAuthManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class UserAuth(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    # Adicione outros campos, se necessário

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAuthManager()

    USERNAME_FIELD = 'username'
    # Adicione outros campos, se necessário

    def __str__(self):
        return self.username

