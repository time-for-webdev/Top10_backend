# Generated by Django 4.1.7 on 2023-03-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0085_remove_vpnlist_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpnlist',
            name='specification',
            field=models.ManyToManyField(to='vpn.specification'),
        ),
    ]