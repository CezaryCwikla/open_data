from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Organisation(models.Model):
    title = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Dataset(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #todo test SET NULL CZY DZIALA
    availability = models.CharField(max_length=20)
    tags = TaggableManager()
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True) #todo test SET NULL CZY DZIALA
    categories = models.ManyToManyField(Category)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.title
