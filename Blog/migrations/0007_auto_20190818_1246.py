# Generated by Django 2.2.3 on 2019-08-18 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20190818_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='Image',
        ),
    ]
