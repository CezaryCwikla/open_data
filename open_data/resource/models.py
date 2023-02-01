from django.db import models

choices = [('Prywatne', 'Prywatne'),
           ('Publiczne', 'Publiczne')]


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.author.user.id, filename)


class Resource(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)
    availability = models.CharField(max_length=20, choices=choices, default='Prywatne')
    # file = models.FileField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.title