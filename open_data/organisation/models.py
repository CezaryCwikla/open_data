from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.shortcuts import reverse
from PIL import Image


class Organisation(models.Model):
    title = models.CharField(max_length=80)
    phone = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=80, null=True)
    email = models.EmailField(max_length=50)
    categories = models.ManyToManyField(Category)
    users = models.ManyToManyField(User)
    image = models.ImageField(default='herb Rzeszowa.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('organisation-detail', kwargs={'pk': self.pk})