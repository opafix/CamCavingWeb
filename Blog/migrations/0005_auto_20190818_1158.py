# Generated by Django 2.2.3 on 2019-08-18 11:58

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20190818_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to=Blog.models.get_image_filename),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]