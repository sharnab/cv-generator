# Generated by Django 5.2.4 on 2025-07-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_cv', '0002_info_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
