# Generated by Django 3.0.4 on 2020-06-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0005_auto_20200611_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='nc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='nl',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nfollowers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nfollowing',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nposts',
        ),
    ]
