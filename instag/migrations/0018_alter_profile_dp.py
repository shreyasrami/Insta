# Generated by Django 3.2.2 on 2022-07-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0017_alter_profile_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, default='post_images/dp_meirma', null=True, upload_to='post_images'),
        ),
    ]
