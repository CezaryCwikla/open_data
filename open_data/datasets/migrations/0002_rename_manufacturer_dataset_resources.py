# Generated by Django 4.1.5 on 2023-01-30 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='manufacturer',
            new_name='resources',
        ),
    ]
