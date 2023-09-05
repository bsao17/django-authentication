from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=25, unique=True, blank=False)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default="1")
    name = models.CharField(max_length=255, default="1")
    avatar = models.ImageField(upload_to="login/static/profile_images", blank=True, null=True)
