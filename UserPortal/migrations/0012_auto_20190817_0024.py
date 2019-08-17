# Generated by Django 2.2.3 on 2019-08-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0011_auto_20190816_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Member', 'MEMBER'), ('President', 'PRESIDENT'), ('Senior Treasurer', 'SENIOR TREASURER'), ('Junior Treasurer', 'JUNIOR TREASURER'), ('Secretary', 'SECRETARY'), ('Tackle Master', 'TACKLE MASTER'), ('Meets Secretary', 'MEETS SECRETARY'), ('Social Secretary', 'SOCIAL SECRETARY')], max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour_1',
            field=models.CharField(blank=True, choices=[('Black', 'BLACK'), ('Brown', 'BROWN'), ('Red', 'RED'), ('Orange', 'ORANGE'), ('Yellow', 'YELLOW'), ('Green', 'GREEN'), ('Blue', 'BLUE'), ('Purple', 'PURPLE'), ('Grey', 'GREY'), ('White', 'WHITE'), ('Warth', 'EARTH'), ('Other', 'OTHER')], default='', max_length=6, verbose_name='Gear Tape Colour 1'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour_2',
            field=models.CharField(blank=True, choices=[('Black', 'BLACK'), ('Brown', 'BROWN'), ('Red', 'RED'), ('Orange', 'ORANGE'), ('Yellow', 'YELLOW'), ('Green', 'GREEN'), ('Blue', 'BLUE'), ('Purple', 'PURPLE'), ('Grey', 'GREY'), ('White', 'WHITE'), ('Warth', 'EARTH'), ('Other', 'OTHER')], default='', max_length=6, verbose_name='Gear Tape Colour 2'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour_3',
            field=models.CharField(blank=True, choices=[('Black', 'BLACK'), ('Brown', 'BROWN'), ('Red', 'RED'), ('Orange', 'ORANGE'), ('Yellow', 'YELLOW'), ('Green', 'GREEN'), ('Blue', 'BLUE'), ('Purple', 'PURPLE'), ('Grey', 'GREY'), ('White', 'WHITE'), ('Warth', 'EARTH'), ('Other', 'OTHER')], default='', max_length=6, verbose_name='Gear Tape Colour 3'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default='3b7ac454e8a24d9f86abce17e5351cc4', max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='rank',
            field=models.ManyToManyField(to='UserPortal.Rank'),
        ),
    ]