# Generated by Django 3.2.2 on 2022-07-09 11:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0018_alter_profile_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
