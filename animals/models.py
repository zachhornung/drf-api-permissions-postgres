
from django.contrib.auth import get_user_model
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)