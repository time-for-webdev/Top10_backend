# Generated by Django 4.1.7 on 2023-03-18 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0054_alter_device_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Device',
            new_name='Devices',
        ),
    ]
