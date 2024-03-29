# Generated by Django 3.2.2 on 2022-07-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0014_auto_20200624_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=None, max_length=25, null=True),
        ),
    ]
