from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    shop_name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=50,null=True)
    Base_url = models.CharField(max_length=100,null=True)
    