from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, UserManager
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    password = models.CharField(max_length=60)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # objects = UserManager()