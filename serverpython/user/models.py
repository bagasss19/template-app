from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, UserManager
# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(
        max_length=50,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True
        )
    password = models.CharField(max_length=60)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()