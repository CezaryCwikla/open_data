# Generated by Django 4.1.5 on 2023-02-02 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('phone', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=80, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('categories', models.ManyToManyField(to='category.category')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
