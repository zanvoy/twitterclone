from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your views here.
class SomeUser(AbstractUser):
   following = models.ManyToManyField("self", blank=True, symmetrical=False)
   test = models.CharField(max_length=42)