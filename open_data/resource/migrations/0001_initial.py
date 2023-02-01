# Generated by Django 4.1.5 on 2023-02-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('availability', models.CharField(choices=[('Prywatne', 'Prywatne'), ('Publiczne', 'Publiczne')], default='Prywatne', max_length=20)),
            ],
        ),
    ]
