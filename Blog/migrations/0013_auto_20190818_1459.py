# Generated by Django 2.2.4 on 2019-08-18 14:59

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_auto_20190818_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to=Blog.models.get_image_filename),
        ),
    ]
