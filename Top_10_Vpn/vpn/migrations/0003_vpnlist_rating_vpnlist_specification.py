# Generated by Django 4.1.7 on 2023-03-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0002_vpnlist_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpnlist',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vpnlist',
            name='specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]