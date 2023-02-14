from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0004_remove_dataset_resources'),
    ]

    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]
