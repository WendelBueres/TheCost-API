from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.TextField(max_length=60)
    last_name = models.TextField(max_length=60)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


