# Generated by Django 2.2.3 on 2019-08-18 13:24

import Blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_auto_20190818_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=Blog.models.get_image_filename)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post')),
            ],
        ),
    ]
