from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Organisation(models.Model):
    title = models.CharField(max_length=80)
    phone = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=80, null=True)
    email = models.EmailField(max_length=50)
    categories = models.ManyToManyField(Category)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
