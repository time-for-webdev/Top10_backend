# Generated by Django 4.1.7 on 2023-05-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0023_alter_device_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Specification1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='device',
            name='Specification2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='device',
            name='Specification3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='device',
            name='Specification4',
            field=models.CharField(default='', max_length=200),
        ),
    ]
