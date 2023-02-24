from django.db import models
from django.shortcuts import reverse
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    title = models.CharField(max_length=80, unique=True)
    file = models.FileField(upload_to='static/icons',
                            validators=[FileExtensionValidator(['svg'])],
                            default='static/icons/government-building-svgrepo-com.svg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-home')
