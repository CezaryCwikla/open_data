from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from organisation.models import Organisation
from category.models import Category
from django.shortcuts import reverse

choices = [('Prywatne', 'Prywatne'),
           ('Publiczne', 'Publiczne')]


class Dataset(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #todo test SET NULL CZY DZIALA
    availability = models.CharField(max_length=20, choices=choices, default='Prywatne')
    frequency = models.IntegerField(default=0)
    tags = TaggableManager()
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True) #todo test SET NULL CZY DZIALA
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('datasets-detail', kwargs={'pk': self.pk})