# Generated by Django 5.2.4 on 2025-07-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_cv', '0004_info_created_at_info_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='languages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
