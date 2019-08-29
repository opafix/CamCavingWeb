# Generated by Django 2.2.3 on 2019-08-26 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0014_auto_20190826_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transactiongroup',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='transaction_group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='Bank.TransactionGroup'),
        ),
    ]
