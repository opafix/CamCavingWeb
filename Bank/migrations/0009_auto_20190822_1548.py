# Generated by Django 2.2.4 on 2019-08-22 14:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0008_auto_20190822_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_key',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100),
        ),
    ]