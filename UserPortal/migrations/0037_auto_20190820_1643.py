# Generated by Django 2.2.4 on 2019-08-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0036_auto_20190819_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='committee',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='emergency_contact_name',
            field=models.CharField(blank=True, help_text='See information below on use of emergency contact information.', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='emergency_phone_number',
            field=models.CharField(blank=True, help_text='See information below on use of emergency contact information.', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mailing_list',
            field=models.BooleanField(default=False, help_text='This is how most club business is conducted. It is highly recommended that you subscribe. If you are already subscribed and leave this box unchecked, you will be unsubscribed.', verbose_name='Subscribe to Mailing List?'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='See information below on use of emergency contact information.', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rank',
            field=models.ManyToManyField(blank=True, null=True, to='UserPortal.Rank', verbose_name='Club Position'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default='c0a00213285b4d12884da9686e647564', max_length=32),
        ),
        migrations.DeleteModel(
            name='LegacyUser',
        ),
    ]
