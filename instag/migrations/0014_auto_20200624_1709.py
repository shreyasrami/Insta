# Generated by Django 3.0.4 on 2020-06-24 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instag', '0013_profile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='instag.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instag.Profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='likedby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instag.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, default='post_images/dp.png', null=True, upload_to='post_images'),
        ),
    ]
