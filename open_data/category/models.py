from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-home')