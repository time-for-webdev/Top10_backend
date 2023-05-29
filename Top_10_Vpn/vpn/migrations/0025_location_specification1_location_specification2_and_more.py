# Generated by Django 4.1.7 on 2023-05-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0024_device_specification1_device_specification2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Specification1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='Specification2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='Specification3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='Specification4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='Specification1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='Specification2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='Specification3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='Specification4',
            field=models.CharField(default='', max_length=200),
        ),
    ]