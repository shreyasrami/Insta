# Generated by Django 3.2.2 on 2022-07-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0015_auto_20220708_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/dqlxnh9bs/image/upload/v1657356235/media/post_images/destination_1_bgmnpc.jpg', null=True, upload_to='post_images'),
        ),
    ]