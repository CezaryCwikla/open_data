from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datasets.models import Dataset



choices = [('Prywatne', 'Prywatne'),
           ('Publiczne', 'Publiczne')]


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.author.user.id, filename)


class Resource(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #todo test SET NULL CZY DZIALA
    availability = models.CharField(max_length=20, choices=choices, default='Prywatne')
    file = models.FileField(upload_to='resources/', null=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('datasets-detail', kwargs={'pk': self.dataset.pk})