# Generated by Django 4.1.5 on 2023-02-24 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='file',
            field=models.FileField(default='static/icons/government-building-svgrepo-com.svg', upload_to='static/icons', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
